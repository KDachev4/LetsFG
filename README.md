# BoostedTravel

Agent-native flight search & booking API. Search 400+ airlines, book tickets programmatically. Built for autonomous AI agents.

**API Base URL:** `https://api.boostedchat.com`

## Packages

| Package | Install | Description |
|---------|---------|-------------|
| **Python SDK** | `pip install boostedtravel` | Python client for search, book, unlock |
| **JS/TS SDK** | `npm install boostedtravel` | TypeScript client with full type safety |
| **MCP Server** | `npx boostedtravel-mcp` | Model Context Protocol server for Claude, etc. |

## Quick Start

### Python

```python
from boostedtravel import BoostedTravel

bt = BoostedTravel(api_key="trav_...")
flights = bt.search("LHR", "JFK", "2026-04-15")
print(f"{flights.total_results} offers, cheapest: {flights.cheapest.summary()}")
```

### JavaScript / TypeScript

```typescript
import { BoostedTravel } from 'boostedtravel';

const bt = new BoostedTravel({ apiKey: 'trav_...' });
const flights = await bt.searchFlights({ origin: 'LHR', destination: 'JFK', dateFrom: '2026-04-15' });
console.log(`${flights.totalResults} offers`);
```

### MCP Server (Claude Desktop / Cursor)

Add to your MCP config:

```json
{
  "mcpServers": {
    "boostedtravel": {
      "command": "npx",
      "args": ["-y", "boostedtravel-mcp"],
      "env": {
        "BOOSTEDTRAVEL_API_KEY": "trav_your_api_key"
      }
    }
  }
}
```

## Get an API Key

```bash
curl -X POST https://api.boostedchat.com/api/v1/agents/register \
  -H "Content-Type: application/json" \
  -d '{"agent_name": "my-agent", "email": "you@example.com"}'
```

## API Docs

- **OpenAPI/Swagger:** https://api.boostedchat.com/docs
- **Agent discovery:** https://api.boostedchat.com/.well-known/ai-plugin.json

## Pricing

| Action | Cost |
|--------|------|
| Search flights | **Free** |
| Unlock offer (confirm price) | $1.00 |
| Book flight | Ticket price + 2.5% service fee |

## Links

- **PyPI:** https://pypi.org/project/boostedtravel/
- **npm (JS SDK):** https://www.npmjs.com/package/boostedtravel
- **npm (MCP):** https://www.npmjs.com/package/boostedtravel-mcp

## License

MIT
