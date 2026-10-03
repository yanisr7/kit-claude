#!/usr/bin/env node
// MCP "search-x" : recherche sur X/Twitter via l'API xAI (Grok + outil x_search).
// Clé : variable d'environnement XAI_API_KEY (https://console.x.ai).
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const MODEL = process.env.SEARCH_X_MODEL || "grok-4-1-fast";

async function searchX(query, days = 30) {
  const key = process.env.XAI_API_KEY;
  if (!key) throw new Error("XAI_API_KEY manquante (voir README du kit).");
  const to = new Date(), from = new Date();
  from.setDate(from.getDate() - days);
  const d = (x) => x.toISOString().split("T")[0];
  const res = await fetch("https://api.x.ai/v1/responses", {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${key}` },
    body: JSON.stringify({
      model: MODEL,
      input: `You are an X/Twitter search assistant. Search X and return real tweets with usernames, content, dates, and links. Be thorough but concise.

Search X/Twitter for: ${query}

Return actual tweets with:
- @username (display name)
- Tweet content
- Date
- Link to tweet

Only include REAL posts. If none found, say so clearly.`,
      tools: [{ type: "x_search", x_search: { from_date: d(from), to_date: d(to) } }],
    }),
  });
  if (!res.ok) throw new Error(`API xAI ${res.status} : ${(await res.text()).slice(0, 400)}`);
  const data = await res.json();
  let text = "", links = new Set();
  for (const item of data.output || []) {
    if (item.type !== "message") continue;
    for (const c of item.content || []) {
      if (c.type === "output_text" && c.text) text = c.text;
      for (const a of c.annotations || []) if (a.type === "url_citation" && /x\.com|twitter\.com/.test(a.url)) links.add(a.url);
    }
  }
  return (text || "Aucun résultat.") + (links.size ? "\n\nSources :\n" + [...links].slice(0, 15).join("\n") : "");
}

const server = new Server({ name: "search-x", version: "1.0.0" }, { capabilities: { tools: {} } });
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: "search_x",
    description: "Search X/Twitter for tweets, trends and discussions using Grok",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "Search query" },
        days: { type: "number", description: "Number of days back (default 30)" },
      },
      required: ["query"],
    },
  }],
}));
server.setRequestHandler(CallToolRequestSchema, async (req) => {
  const { query, days } = req.params.arguments || {};
  try {
    return { content: [{ type: "text", text: await searchX(query, days) }] };
  } catch (e) {
    return { content: [{ type: "text", text: "Erreur : " + e.message }], isError: true };
  }
});
await server.connect(new StdioServerTransport());
