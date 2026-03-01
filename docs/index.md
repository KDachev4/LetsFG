---
hide:
  - navigation
  - toc
---

<div class="hero-section" markdown>

# BoostedTravel

<p class="hero-tagline">Flight search & booking for AI agents and developers. 400+ airlines, straight from the terminal.</p>

<div class="install-cmd"><span class="prompt">$</span> pip install boostedtravel</div>

<div class="hero-actions">
<a href="getting-started/" class="btn-primary">Get started</a>
<a href="api-guide/" class="btn-ghost">API guide</a>
<a href="https://api.boostedchat.com/docs" class="btn-ghost">Swagger</a>
</div>

</div>

---

<div class="cards-grid">

<a class="card" href="getting-started/">
<span class="card-icon">→</span>
<h3>Getting Started</h3>
<p>Register, auth, payment setup — first flight in 5 minutes.</p>
</a>

<a class="card" href="api-guide/">
<span class="card-icon">→</span>
<h3>API Guide</h3>
<p>Search results, error handling, workflows, unlock mechanics.</p>
</a>

<a class="card" href="agent-guide/">
<span class="card-icon">→</span>
<h3>AI Agent Guide</h3>
<p>Architecture, preference scoring, rate limits, price tracking.</p>
</a>

<a class="card" href="cli-reference/">
<span class="card-icon">→</span>
<h3>CLI Reference</h3>
<p>Commands, flags, cabin codes — full terminal reference.</p>
</a>

<a class="card" href="packages/">
<span class="card-icon">→</span>
<h3>Packages</h3>
<p>Python SDK, JavaScript SDK, MCP Server for Claude & Cursor.</p>
</a>

<a class="card" href="https://api.boostedchat.com/docs">
<span class="card-icon">→</span>
<h3>OpenAPI Reference</h3>
<p>Interactive Swagger docs — try every endpoint in your browser.</p>
</a>

</div>

---

<p class="section-label">How it works</p>

<div class="flow">
<span class="flow-step">Search <small>free</small></span>
<span class="flow-arrow">→</span>
<span class="flow-step">Unlock <small>$1</small></span>
<span class="flow-arrow">→</span>
<span class="flow-step">Book <small>free</small></span>
</div>

1. **Search** — real-time offers with price, airlines, duration, stopovers. Free and unlimited.
2. **Unlock** — confirms the live price with the airline, reserves for 30 min. $1 flat.
3. **Book** — creates real PNR. E-ticket sent to passenger email. Free after unlock.

---

<p class="section-label">Pricing</p>

## BoostedTravel vs Flight Websites

| | Google Flights / Booking / Expedia | **BoostedTravel** |
|---|---|---|
| Search | Free | **Free** |
| View details | Free (with tracking) | **Free** (no tracking) |
| Book | Ticket + hidden markup | **$1 unlock + ticket** |
| Price goes up on repeat search? | Yes | **Never** |

---

<p class="section-label">Quick example</p>

## Search → Unlock → Book

=== "CLI"

    ```bash
    boostedtravel search LHR JFK 2026-04-15
    boostedtravel unlock off_xxx
    boostedtravel book off_xxx \
      --passenger '{"id":"pas_0","given_name":"John","family_name":"Doe","born_on":"1990-01-15","gender":"m","title":"mr"}' \
      --email john.doe@example.com
    ```

=== "Python"

    ```python
    from boostedtravel import BoostedTravel

    bt = BoostedTravel(api_key="trav_...")
    flights = bt.search("LHR", "JFK", "2026-04-15")

    unlocked = bt.unlock(flights.offers[0].id)
    booking = bt.book(
        offer_id=unlocked.offer_id,
        passengers=[{"id": "pas_0", "given_name": "John",
                     "family_name": "Doe", "born_on": "1990-01-15",
                     "gender": "m", "title": "mr"}],
        contact_email="john.doe@example.com",
    )
    ```

=== "JavaScript"

    ```typescript
    import { BoostedTravel } from 'boostedtravel';

    const bt = new BoostedTravel({ apiKey: 'trav_...' });
    const flights = await bt.search('LHR', 'JFK', '2026-04-15');
    ```

=== "MCP Config"

    ```json
    {
      "mcpServers": {
        "boostedtravel": {
          "command": "npx",
          "args": ["-y", "boostedtravel-mcp"],
          "env": { "BOOSTEDTRAVEL_API_KEY": "trav_..." }
        }
      }
    }
    ```
