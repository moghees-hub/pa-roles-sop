# Renders role.html: the Head of Operations and Analytics proposal for George and Callum.
# Shares the look of index.html. Run: python role_build.py
import html
from pathlib import Path

from build import CSS

HERE = Path(__file__).parent
e = html.escape

UPDATED = "For the meeting on 28 October 2026"

D = {
    "Lead Tracker": "https://leads.physiqueacademy.com",
    "Booked Calls": "https://source.physiqueacademy.com/#calls",
    "Lead Chase": "https://leadchase.physiqueacademy.com",
    "Sales Dashboard": "https://sales.physiqueacademy.com",
    "Commission Tracker": "https://commission-tracker-production-18a6.up.railway.app",
    "HYROS": "https://source.physiqueacademy.com",
    "Incoming Revenue": "https://stripe-overview-dashboard-production.up.railway.app",
    "Failed Payments": "https://web-production-b6f83.up.railway.app",
    "Disputes": "https://radiant-reprieve-production.up.railway.app/dashboard",
    "6-Month Renewals": "https://6-month-renewal-production.up.railway.app",
    "My Clients": "https://myclients.physiqueacademy.com",
    "Coach Hub": "https://coach.physiqueacademy.com",
    "Command Center": "https://hub.physiqueacademy.com",
}


def src(name):
    url = D.get(name)
    return f'<a href="{url}" target="_blank" rel="noopener">{e(name)}</a>' if url else e(name)


OWNS = [
    ("One scorecard", "Every number the business runs on, in one place, locked every Monday for the week before."),
    ("Accountability", "Each number has an owner and a target. When it is off target, the owner brings the reason and the fix."),
    ("Weekly calls", "I run a short call with each area (lead gen, sales, marketing, revenue) and a weekly review with George and Callum."),
    ("The systems behind it", "I keep the dashboards and automations that feed the numbers accurate and running, and build what is missing."),
]

# (area, owner, [(metric, source)])
SCORECARD = [
    ("Lead gen", "Callum and setters (Patrick, Amani, Jan)", [
        ("New leads", "Lead Tracker"),
        ("Booked calls and booking rate", "Booked Calls"),
        ("Show rate", "Booked Calls"),
        ("Leads chased and recovered", "Lead Chase"),
    ]),
    ("Sales", "Sales team", [
        ("Calls taken", "Sales Dashboard"),
        ("Closes and close rate, per rep", "Sales Dashboard"),
        ("Cash collected", "Sales Dashboard"),
        ("Commission per rep", "Commission Tracker"),
    ]),
    ("Marketing", "Callum", [
        ("Ad spend", "HYROS"),
        ("Cost per lead and per booked call", "HYROS"),
        ("Sales and revenue by source", "HYROS"),
    ]),
    ("Revenue and retention", "George and me, head coaches for retention", [
        ("Money in (UK, US, UAE)", "Incoming Revenue"),
        ("Active clients and churn", "My Clients"),
        ("Failed payments and recovered", "Failed Payments"),
        ("Disputes and refunds", "Disputes"),
        ("Renewals due", "6-Month Renewals"),
        ("Retention by coach", "Coach Hub"),
    ]),
]

RHYTHM = [
    ("Monday", "Scorecard locked", "Me", "Last week's numbers pulled into one place and shared before any call"),
    ("Tuesday", "Lead gen call", "Callum, setters, me", "Leads, bookings, show rate, chase list"),
    ("Tuesday", "Sales call", "Sales team, me", "Calls, closes, close rate, cash, per rep"),
    ("Wednesday", "Marketing call", "Callum, me", "Spend, cost per lead, what is working by source"),
    ("Wednesday", "Revenue and retention", "George, me", "Money in, churn, failed payments, disputes, coach retention"),
    ("Thursday", "Weekly review", "George, Callum, me", "Whole scorecard, what is off target, actions agreed"),
    ("Friday", "Actions chased", "Me", "Every action from the week checked against its owner and deadline"),
]

ACCOUNT = [
    ("Every number has one owner", "Not a team. One name, so it is clear who answers for it."),
    ("Every number has a target", "Set by George. Green on target, amber close, red off target."),
    ("Red means a reason and a fix", "The owner brings both to their weekly call, not just the number."),
    ("Every fix gets an action", "Written down with an owner and a deadline, checked the following week."),
    ("Repeat reds go to George", "Two weeks red in a row comes up in the weekly review."),
]

NEED = [
    ("Targets", "A weekly target for each number on the scorecard, so we measure against something."),
    ("Owners confirmed", "Agree who owns each area (draft owners are in the scorecard below)."),
    ("Call times", "Fixed slots each week for the calls, so they become routine."),
    ("What comes off my plate", "Decide which current jobs (website builds, design, clothing, admin) move to someone else or stop, so this role gets the time it needs."),
]

FIRST_MONTH = [
    ("Week 1", "Agree targets, owners and call times. I build the first scorecard by hand from the dashboards."),
    ("Week 2", "First full week of calls. Find the gaps: numbers we cannot see yet or do not trust."),
    ("Week 3", "Scorecard page live in the Command Center, filling itself from the dashboards each Monday."),
    ("Week 4", "Review with George and Callum: what to keep, cut or change in the rhythm."),
]


def bullets(items):
    return '<ul class="list">' + "".join(f"<li><b>{e(a)}</b><span>{e(t)}</span></li>" for a, t in items) + "</ul>"


def flow(items):
    return '<ol class="flow">' + "".join(f"<li><b>{e(a)}</b>{e(t)}</li>" for a, t in items) + "</ol>"


def section(id_, eyebrow, title, body, intro=""):
    p = f"<p>{e(intro)}</p>" if intro else ""
    return f'<section class="part" id="{id_}"><div class="eyebrow">{e(eyebrow)}</div><h2>{e(title)}</h2>{p}{body}</section>'


def scorecard():
    out = []
    for area, owner, rows in SCORECARD:
        trs = "".join(f"<tr><td>{e(m)}</td><td>{src(s)}</td><td class='tbc'>To set</td></tr>" for m, s in rows)
        out.append(
            f'<div class="group"><h3>{e(area)} <span class="own">Owner: {e(owner)}</span></h3>'
            f'<div class="table-wrap"><table><thead><tr><th>Number</th><th>Where it comes from</th><th>Weekly target</th></tr></thead>'
            f"<tbody>{trs}</tbody></table></div></div>")
    return "".join(out)


def rhythm():
    trs = "".join(f"<tr><td>{e(d)}</td><td><b>{e(c)}</b></td><td>{e(w)}</td><td>{e(x)}</td></tr>" for d, c, w, x in RHYTHM)
    return f'<div class="table-wrap"><table><thead><tr><th>Day</th><th>What</th><th>Who</th><th>Covers</th></tr></thead><tbody>{trs}</tbody></table></div>'


def sources():
    names = [n for n in D if n != "Command Center"]
    links = "".join(f'<a class="chip" href="{D[n]}" target="_blank" rel="noopener">{e(n)}</a>' for n in names)
    return f'<div class="chips">{links}</div>'


EXTRA_CSS = """
.group h3 .own { font-size: 12px; letter-spacing: 0; text-transform: none; font-weight: 500; color: var(--muted); margin-left: 8px; }
td.tbc { color: var(--amber); font-weight: 600; }
td a, .chip { color: var(--blue); text-decoration: none; font-weight: 600; }
td a:hover { text-decoration: underline; }
.chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip { font-size: 14px; background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 8px 12px; }
.chip:hover { border-color: var(--blue); }
.lead { font-size: 17px; max-width: 70ch; }
.quote { background: var(--surface); border: 1px solid var(--line); border-left: 4px solid var(--green); border-radius: 10px; padding: 14px 16px; font-size: 15px; }
.quote b { color: var(--accent); }
"""


def build():
    toc_items = [("why", "Why", "Why this role"), ("owns", "The role", "What I own"),
                 ("scorecard", "Scorecard", "The weekly scorecard"), ("rhythm", "Rhythm", "The weekly rhythm"),
                 ("accountability", "Rules", "How accountability works"), ("built", "Already built", "Where the data comes from"),
                 ("need", "Decisions", "What I need from you"), ("month", "Plan", "The first month")]
    toc = "".join(f'<li><a href="#{i}"><span>{e(a)}</span><em>{e(b)}</em></a></li>' for i, a, b in toc_items)
    parts = "".join([
        section("why", "Why", "Why this role",
                '<div class="quote">George: <b>"Head of operations, analytics, data, everything all in one place.</b> '
                'Bring the data, hold people accountable to that data, bring it all together, and each week we go through it."</div>',
                "With Harry gone and Callum on marketing, nobody is holding the numbers together. This puts one person on it, with a fixed weekly rhythm."),
        section("owns", "The role", "Head of Operations and Analytics: what I own", bullets(OWNS)),
        section("scorecard", "Scorecard", "The weekly scorecard", scorecard(),
                "Draft list of numbers, where each one comes from today, and who owns it. Targets to be set together."),
        section("rhythm", "Rhythm", "The weekly rhythm", rhythm(),
                "Short, fixed calls. Days and times to agree."),
        section("accountability", "Rules", "How accountability works", flow(ACCOUNT)),
        section("built", "Already built", "Where the data comes from", sources(),
                "Most of the data is already flowing through dashboards I have built. Click any of them to open it. The job now is pulling them into one scorecard and running the weeks off it."),
        section("need", "Decisions", "What I need from George and Callum", bullets(NEED)),
        section("month", "Plan", "The first month", flow(FIRST_MONTH)),
    ])
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>Operations and Analytics Role</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<style>{CSS}{EXTRA_CSS}</style>
</head>
<body>
<header class="top">
  <div class="top-in">
    <img class="logo" src="pa-logo-white.png" alt="Physique Academy" width="120" height="72">
    <h1><span class="hl">Head of Operations and Analytics:</span> the numbers, in one place, every week</h1>
    <div class="sub">Proposal by Moghees Siddique &middot; {e(UPDATED)}</div>
  </div>
</header>
<main>
  <p class="lead">One person owns the numbers across lead gen, sales, marketing and revenue, brings them together every Monday, and holds each area to its targets through a short weekly call. George, Callum and I review the whole picture once a week and agree the actions.</p>
  <nav class="toc" aria-label="On this page"><h2>On this page</h2><p class="hint">Click a section to jump straight to it.</p><ol>{toc}</ol></nav>
  {parts}
  <div class="cc"><p><b>Current role and systems</b> are on the Roles and Responsibilities page.</p><a class="btn" href="./">Open Roles and Responsibilities</a></div>
  <footer>Proposal, Physique Academy &middot; {e(UPDATED)}. No passwords or keys are kept on this page.</footer>
</main>
</body>
</html>
"""
    (HERE / "role.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    build()
