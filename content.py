# Single source for both outputs: build.py renders this to index.html (web) and a .docx (Word).
# Block types: ("p", text) ("bullets", [(lead, text), ...]) ("table", headers, rows)
#              ("flow", [(title, text), ...]) ("systems", [group, ...]) ("stats", [(big, label), ...])
#              ("h3", text) ("note", text)
# No em dashes anywhere in the copy.

TITLE = "Moghees Siddique"
SUBTITLE = "Roles, responsibilities and systems at Physique Academy"
UPDATED = "Updated 27 October 2026"
COMMAND_CENTER = "https://hub.physiqueacademy.com"

# Each stat opens a list when clicked. A string source pulls the list from the content below:
# "systems" = every system card, "platforms" = the platforms table, "reports" = the "What runs when" table.
STATS = [
    ("28", "systems I built and run, online 24/7", "systems"),
    ("3", "Stripe accounts: UK, US and UAE", [
        "UK account",
        "US account (Physique Coaching LLC, our Wyoming company)",
        "UAE account",
    ]),
    ("20+", "platforms I manage, including accounts, access and costs", "platforms"),
    ("10+", "automatic reports and alerts going out every day", "reports"),
]

SECTIONS = [
    {
        "id": "overview", "eyebrow": "Start here", "title": "Overview",
        "blocks": [
            ("p", "I look after the technical and operational side of Physique Academy: the systems the business runs on, "
                  "the payments set-up across our three Stripe accounts, the marketing and tracking stack, the website, "
                  "design work and the clothing operation. On top of that I'm the day-to-day point of contact for the coaching team."),
            ("p", "This page is set out so you can read it at two levels. Sections 1 to 3 give the big picture: how everything connects, "
                  "what runs when, and what I check. Section 4 is the reference part: one card per system saying what it does, "
                  "who uses it, when it runs and what happens if it stops."),
            ("h3", "Hours and availability"),
            ("p", "My work runs across a long window rather than fixed office hours. Coach queries, client issues and system problems "
                  "come in at all hours and across time zones, so I stay reachable outside normal working time and deal with anything "
                  "urgent when it happens rather than the next morning."),
        ],
    },
    {
        "id": "chain", "eyebrow": "Section 1", "title": "How it all connects: from a booked call to a looked-after client",
        "blocks": [
            ("p", "This is what happens for a single client, start to finish. I built every step and I'm across it every day."),
            ("flow", [
                ("A lead books a call", "They land on one of the landing or booking pages I built and pick a slot on the GoHighLevel calendar "
                 "for that channel. Their intake answers and where they came from are saved against their contact."),
                ("The team is told instantly", "The New Bookings bot posts a card into #new-bookings with the lead's details and answers, "
                 "and DMs the assigned salesperson so they can prepare."),
                ("It shows in the morning briefing", "At 9am the Daily Stats bot posts that day's confirmed calls per salesperson into #sales, "
                 "each one linked to its booking card."),
                ("The call happens", "The salesperson marks the outcome with one emoji on the booking card (closed, thinking, lost, no-show, cancelled) "
                 "and the GoHighLevel pipeline moves by itself. If the call is recorded in Fathom, an AI summary is posted for review."),
                ("The sale is made", "Payment goes through Stripe (UK, US or UAE). From that one payment: a sale alert posts to Slack, the Sales Dashboard "
                 "records it, the Booked Calls Tracker matches it back to the call, the Commission Tracker credits the salesperson, and "
                 "Incoming Revenue counts it as new cash in GBP."),
                ("The client gets a coach", "The client is allocated to a coach on Trello. The coach gets an email with the client's details, "
                 "the client gets their welcome email, and the Master Tracker and ChartMogul are updated, all by my Coach Allocation system "
                 "(which replaced the old Zaps and ActiveCampaign automation)."),
                ("End of day", "At 11:55pm the Daily Stats bot posts the end-of-day sales report: what was sold, by whom, for how much."),
                ("From then on, the systems look after them", "They appear in their coach's My Clients list with live payment status. Milestones flag "
                 "them at 3 and 5 months. A failed payment alerts the team straight away. If they're due to cancel, the coach sees a warning. "
                 "Their history feeds the retention reports and the weekly and monthly client tallies."),
            ]),
        ],
    },
    {
        "id": "rhythm", "eyebrow": "Section 2", "title": "What runs when",
        "blocks": [
            ("p", "Everything below runs by itself. My job is to make sure each one went out correctly, and to fix it the same day if it didn't. "
                  "Times are UK time unless stated."),
            ("table", ["When", "What goes out", "Where it goes"], [
                ["As it happens", "New booking cards, sale alerts, failed payments and recoveries, cancellation requests, disputes (UAE and US)", "Slack channels and DMs"],
                ["Every 5 minutes", "Fathom checks for new call recordings and posts summaries; Failed Payments checks all three Stripe accounts", "#fathom-meetings, head coaches channel, #failed-payments"],
                ["Every 15 minutes", "Disputes dashboard checks all three Stripe accounts for new chargebacks", "#client-disputes"],
                ["Daily, 8am Bali", "Incoming Revenue summary (yesterday and month so far); Lead Gen report (calls booked, sales, show rate per setter)", "DM to you (and Callum for Lead Gen)"],
                ["Daily, 9am", "Morning briefing of today's confirmed calls; PIF renewal reminders to coaches; staff anniversary check", "#sales; DMs to coaches; DM to you a week before an anniversary"],
                ["Daily, 11:55pm", "End-of-day sales report with AI insight", "#sales"],
                ["Monday, 9am", "Coach Hub audit: failed emails, missing backups, requests left over 7 days", "To me (Slack and email)"],
                ["Friday, 9am", "Weekly review of how each head coach ran their 1:1s, plus each head coach's own section by DM", "Head coaches channel and DMs"],
                ["Sunday, 11:45pm", "Weekly New / Lost / Net client tally per coach", "Private tally channel (you, Bailey and me)"],
                ["1st of the month, 9am", "Monthly client tally per coach with 3, 6 and 12 month trends", "Private tally channel"],
            ]),
        ],
    },
    {
        "id": "checks", "eyebrow": "Section 3", "title": "What I do day to day",
        "blocks": [
            ("bullets", [
                ("Morning checks", "Confirm the overnight and morning reports went out and the numbers look right. If one is missing or wrong, I find out why and re-send it."),
                ("Coach and head coach support", "I'm the first point of contact for the coaches and head coaches all day, every day: client account queries, access problems, "
                 "chasing requests, and help with any of our systems."),
                ("Requests inbox", "Work through Coach Hub submissions (plan changes, pauses, issues, holidays) and make sure each one reaches the right person and gets actioned."),
                ("Payments", "Watch failed payments, disputes and cancellations as they come in; set up payment links, plan changes, free months and moves between Stripe accounts."),
                ("Fixes and changes", "Fix anything that breaks the same day. Platforms like Stripe, Slack, GoHighLevel and Fathom change how they work without warning, "
                 "and that silently breaks things if nobody is watching."),
                ("New work", "Build the new systems, reports and pages you and the team ask for (see Section 15 for what's in progress)."),
            ]),
        ],
    },
    {
        "id": "systems", "eyebrow": "Section 4", "title": "The systems, one by one",
        "blocks": [
            ("p", "Each card says what the system does, who uses it, when it runs, and what happens if it stops. All of them run on Railway "
                  "(our cloud hosting) and their code is saved in GitHub."),
            ("systems", [
                {"name": "Money and payments", "items": [
                    {"name": "Sales Dashboard", "parts": 2, "where": "sales.physiqueacademy.com", "status": "Live",
                     "what": "Live record of every new sale across UK, US and UAE Stripe. A separate recorder listens to Stripe and writes each sale with its salesperson and lead source.",
                     "who": "You, sales team, me", "when": "Instantly on each sale",
                     "stop": "New sales stop appearing. Stripe still takes the money; I re-sync the missing rows."},
                    {"name": "Incoming Revenue", "where": "Private dashboard", "status": "Live",
                     "what": "Cash in across all three Stripe accounts in GBP: new cash, recurring cash, refunds, cancellations, failed payments and recovery, plus monthly cash charts.",
                     "who": "You", "when": "Live, plus a daily summary at 8am Bali",
                     "stop": "Dashboard or summary missing. No money is affected."},
                    {"name": "Failed Payments", "where": "#failed-payments", "status": "Live",
                     "what": "Alerts the moment a client payment fails, and again when it's recovered, with the coach's name.",
                     "who": "Team, coaches", "when": "Every 5 minutes",
                     "stop": "Failed payments go unnoticed and aren't chased."},
                    {"name": "Disputes", "where": "#client-disputes", "status": "Live",
                     "what": "Tracks every chargeback and its deadline, posts UAE and US disputes to Slack and DMs the coach. (UK disputes still post via a Zapier zap.)",
                     "who": "Whoever handles disputes, coaches", "when": "Every 15 minutes",
                     "stop": "Disputes can miss their evidence deadline."},
                    {"name": "Commission Tracker", "where": "Private dashboard", "status": "Live",
                     "what": "Works out commission per salesperson from the sales record.",
                     "who": "You, sales team", "when": "Live", "stop": "Commission figures go stale until fixed."},
                    {"name": "6-Month Renewals", "where": "Private dashboard", "status": "Live",
                     "what": "Tracks upcoming renewals and paid-in-full clients, and which ones roll on to monthly.",
                     "who": "Me, you", "when": "Live", "stop": "Renewals aren't flagged in time."},
                    {"name": "PIF renewal reminders", "where": "DM to each coach", "status": "Live",
                     "what": "Tells the coach 30 days before a client's paid-in-full term ends, so the renewal conversation happens in time, and flags clients paying twice.",
                     "who": "Coaches", "when": "Daily, 9am", "stop": "Coaches aren't reminded; the 6-Month Renewals tracker still shows the list."},
                    {"name": "Cancellation system", "parts": 2, "where": "physiqueacademy.com/refunds-cancellations", "status": "Live",
                     "what": "Client cancellation form, checks and routing to the coach, Slack alert, the 7-day notice before each payment, a team guide, and a tracker of who has signed the cancellation policy.",
                     "who": "Clients, coaches, Bailey (actions cancellations in Stripe)", "when": "On every request, and 7 days before every payment",
                     "stop": "We lose the paper trail that wins chargebacks."},
                ]},
                {"name": "Sales and leads", "items": [
                    {"name": "New Bookings bot", "where": "#new-bookings", "status": "Live",
                     "what": "Posts a card for every booked call with the lead's intake answers, DMs the salesperson, and moves the GoHighLevel pipeline when the salesperson reacts with an outcome emoji.",
                     "who": "Sales team", "when": "Instantly on each booking",
                     "stop": "Salespeople go into calls blind and the pipeline stops updating."},
                    {"name": "Daily Stats bot", "where": "#sales", "status": "Live",
                     "what": "9am briefing of today's confirmed calls, and the 11:55pm end-of-day sales report with an AI insight.",
                     "who": "Sales team, you", "when": "9am and 11:55pm daily",
                     "stop": "The team starts the day without a call list and there's no daily wrap-up."},
                    {"name": "Booked Calls Tracker", "where": "bookedcalls.physiqueacademy.com", "status": "Live",
                     "what": "Matches every sale back to its booked call so close rates per salesperson are real.",
                     "who": "You, me", "when": "Live", "stop": "Close rates can't be measured."},
                    {"name": "Lead Tracker and Lead Gen report", "where": "Private dashboard", "status": "Live",
                     "what": "Tracks Instagram DM leads from both inboxes through to booked calls and sales. Sends the daily Lead Gen report: calls booked, sales and £ per setter, show rate, calls waiting on an outcome, and whether we're ahead or behind.",
                     "who": "You, Callum, setters (Patrick, Amani and Jan)", "when": "Live, report at 8am Bali",
                     "stop": "No daily view of setter performance."},
                    {"name": "HYROS dashboard", "where": "Private dashboard", "status": "Live",
                     "what": "Shows where new sales really come from (paid ads, Instagram, organic) and booked-call numbers, using HYROS tracking.",
                     "who": "You, marketing", "when": "Live", "stop": "Less visibility on which channels produce sales."},
                    {"name": "Lead Chase", "where": "Private dashboard", "status": "Live",
                     "what": "Leads who filled in a form but haven't booked a call. Each new one posts to #lead-chase for the lead gen team to chase, and drops off once they book.", "who": "Lead gen team", "when": "Live, booking check every 15 minutes",
                     "stop": "Missed leads aren't followed up."},
                    {"name": "Fathom call summaries", "where": "#fathom-meetings and head coaches channel", "status": "Live",
                     "what": "AI summary of every recorded sales call and head coach 1:1. Head coaches also get their own summaries by DM, and a Friday review of how they ran their 1:1s.",
                     "who": "Sales team, head coaches, you", "when": "Every 5 minutes; review Fridays 9am",
                     "stop": "Calls have to be listened to in full to review them."},
                    {"name": "Short links", "where": "go.physiqueacademy.com", "status": "Live",
                     "what": "Each coach's own Instagram bio link, so bookings from their bio are tracked to them.",
                     "who": "Coaches", "when": "Every click", "stop": "Bio links fall back to the normal booking page, so nothing breaks, but tracking is lost."},
                    {"name": "Form relay", "where": "Behind the website forms", "status": "Live",
                     "what": "Takes sign-ups from our free guide forms and adds them to Klaviyo (and ActiveCampaign until it's switched off), replacing the old Zaps.",
                     "who": "Marketing", "when": "On each sign-up", "stop": "New sign-ups don't get the guide email."},
                ]},
                {"name": "Coaching", "items": [
                    {"name": "Coach Hub", "where": "coach.physiqueacademy.com", "status": "Live",
                     "what": "The coaching team's daily portal: request forms, the submissions inbox, six retention reports, weekly and monthly client tallies, client links and tools, backups and a weekly audit.",
                     "who": "All coaches, head coaches, you", "when": "Live; tallies Sunday and the 1st",
                     "stop": "Coaches can't submit requests. Every submission is also backed up in Google Sheets."},
                    {"name": "My Clients", "where": "myclients.physiqueacademy.com", "status": "Live",
                     "what": "Each coach's live client list with payment status, including a flag on clients due to cancel.",
                     "who": "Coaches, head coaches", "when": "Live", "stop": "Coaches lose sight of payment status."},
                    {"name": "Client Milestones", "where": "Slack", "status": "Live",
                     "what": "Flags clients reaching 3 and 5 months.", "who": "Coaches, team", "when": "Automatic checks",
                     "stop": "Milestone moments are missed."},
                    {"name": "Coach Allocation", "where": "Trello, email, Client Tracker", "status": "Live",
                     "what": "When a new client is moved to a coach on Trello: copies the card to the coach's board, emails the coach, sends the client's welcome email, adds them to the Master Tracker and updates ChartMogul. Also a daily check that marks leavers as Finished. Replaced the coach Zaps and ActiveCampaign.",
                     "who": "You, coaches, new clients", "when": "Every minute",
                     "stop": "New clients wait for their coach. Every step is logged, so anything missed is re-run."},
                ]},
                {"name": "Owner and team", "items": [
                    {"name": "Command Center", "where": "hub.physiqueacademy.com", "status": "Live",
                     "what": "Your private launchpad: one page linking to every dashboard, with a snapshot of the business.",
                     "who": "You only", "when": "Live", "stop": "Dashboards still work directly."},
                    {"name": "Staff anniversaries", "where": "DM to you", "status": "Live",
                     "what": "Reminds you a week before each staff member's work anniversary.",
                     "who": "You", "when": "9am daily check", "stop": "No reminder."},
                    {"name": "Changelog", "where": "Private site", "status": "Live",
                     "what": "History of changes made to the coach dashboards.", "who": "Me, you", "when": "Updated as I go",
                     "stop": "No effect on the business."},
                ]},
                {"name": "Content and clients", "items": [
                    {"name": "Guides reader", "where": "read.physiqueacademy.com", "status": "Live",
                     "what": "Phone-friendly versions of the Lean Bulk and No BS Fat Loss blueprints, unlocked with an email sign-up.",
                     "who": "Leads", "when": "Live", "stop": "The PDF downloads still work."},
                    {"name": "Welcome Tee", "where": "Shopify, email", "status": "Testing",
                     "what": "Sends each new active client a single-use code for a free PA tee on our Shopify store.",
                     "who": "New clients", "when": "Daily", "stop": "Waiting on the warehouse before go-live."},
                ]},
            ]),
        ],
    },
    {
        "id": "platforms", "eyebrow": "Section 5", "title": "Where everything runs: the platforms I manage",
        "blocks": [
            ("p", "I set up and look after all of these, including accounts, access and the ongoing costs."),
            ("table", ["Platform", "What it's for"], [
                ["Railway", "Cloud hosting where all 28 systems run, 24 hours a day, each with its own secure storage."],
                ["GitHub", "Where all the code is stored with a full history, so nothing is lost and any change can be undone."],
                ["Stripe (UK, US, UAE)", "Every subscription, payment, refund and cancellation. The master record of revenue."],
                ["ChartMogul", "Subscription analytics: active clients, new and lost per month, and which coach each client belongs to."],
                ["GoHighLevel (GHL)", "Our CRM: leads, contacts, bookings, calendars, pipelines, forms, workflows and the sales phone line."],
                ["Slack", "Where every alert, report and tally is delivered."],
                ["Google Sheets", "The Client Tracker, Sales Report and backup copies of important records."],
                ["Klaviyo and ActiveCampaign", "Email. Klaviyo holds our 24,900+ subscribers and the guide funnels; ActiveCampaign still runs some booked-call emails until it's switched off."],
                ["Calendly and Typeform", "Bookings and questionnaires for the mental health calls."],
                ["Trello and Zapier", "Coaches' client boards, and the older automations that are being replaced."],
                ["HYROS and Meta", "Ad tracking and paid advertising."],
                ["Craft CMS and Amazon S3", "The physiqueacademy.com website and its image storage."],
                ["Google Search Console", "How the website shows up in Google."],
                ["Fathom", "Call recording, feeding the AI summaries."],
                ["Claude (Anthropic)", "The AI that writes the call summaries, report insights and reviews."],
                ["Shopify", "The clothing store: products, stock and orders."],
                ["GoDaddy and Cloudflare", "Our domains and DNS (the .com and the .co.uk)."],
            ]),
        ],
    },
    {
        "id": "payments", "eyebrow": "Section 6", "title": "Payments and billing (Stripe UK, US and UAE)",
        "blocks": [
            ("bullets", [
                ("Cancellations", "I built and run the whole cancellation flow: the client form, the checking step, routing to the coach, Slack alerts, the 7-day "
                 "notice before payments, the team guide and the policy-signing tracker. Bailey actions the cancellation in Stripe; I make sure nothing is missed."),
                ("Coach requests", "Plan changes, pauses, refunds and transfers from Coach Hub are routed to the right person, logged and followed through."),
                ("Disputes", "I run the Disputes dashboard, pull together evidence and transaction records, and track deadlines. The response itself is submitted in Stripe by whoever handles it."),
                ("Payment links and plan changes", "Payment links for subscriptions and one-off payments in the right account and currency; free months, plan changes and paid-in-full roll-overs."),
                ("Moving clients between accounts", "Moving clients from UK to US Stripe (for example US-based clients) without double-charging them or losing them from ChartMogul."),
                ("Billing audits", "Cross-checking subscriptions across the three accounts, including scheduled future charges that don't show in normal views."),
                ("Subscription site", "billing.physiqueacademy.com, where clients sign up and manage their subscriptions."),
                ("Documents", "The cancellation guide, billing agreements and terms and conditions, in PA branding."),
            ]),
        ],
    },
    {
        "id": "sales", "eyebrow": "Section 7", "title": "Sales, marketing and advertising",
        "blocks": [
            ("bullets", [
                ("Landing pages", "All landing pages: ad variants, booking pages, pricing pages and challenge pages, plus the versions embedded in the main site."),
                ("GoHighLevel", "The whole account: calendars for every booking channel, workflows, intake fields, pipelines and regular clean-ups so the pipeline matches real sales."),
                ("Call outcomes", "Salespeople mark outcomes with an emoji on the booking card and the pipeline moves by itself."),
                ("Ad tracking", "Meta Conversions API via Stape and Google Tag Manager, and HYROS (set up from scratch), so we can see which ads and channels produce sales."),
                ("Source tracking", "Making sure every booking and sale traces back to where it came from, including each coach's own bio link."),
                ("Lead qualification", "Workflows that keep ineligible applicants off the sales calendar."),
                ("Free guide funnels", "The Lean Bulk and No BS Fat Loss guide pages, sign-up forms, Klaviyo emails and the phone-friendly reader."),
            ]),
        ],
    },
    {
        "id": "email", "eyebrow": "Section 8", "title": "Email",
        "blocks": [
            ("bullets", [
                ("Klaviyo", "I moved our 24,900+ subscribers from ActiveCampaign to Klaviyo in June 2026 and manage the account, sending domain, lists and guide email flows."),
                ("ActiveCampaign", "Still runs some booked-call emails. Coach allocation has already moved off it, and the rest is being moved so it can be switched off when it renews on 31 October 2026."),
                ("Calendly and Typeform", "The booking system and questionnaires for the mental health calls."),
            ]),
        ],
    },
    {
        "id": "reporting", "eyebrow": "Section 9", "title": "Reporting and analysis",
        "blocks": [
            ("bullets", [
                ("Daily and weekly reports", "Everything in Section 2, checked to make sure it went out correctly."),
                ("Retention", "Retention, client-stay and per-coach reports for the coaching team."),
                ("Reconciliation", "Keeping Stripe, GoHighLevel and the Sales Report in line so the numbers agree."),
                ("Reports on request", "Recent examples: the AI vs Lead Gen report and the US call coverage report (when prospects book versus when someone is free to take the call)."),
            ]),
        ],
    },
    {
        "id": "website", "eyebrow": "Section 10", "title": "Website, email accounts and IT",
        "blocks": [
            ("bullets", [
                ("physiqueacademy.com", "Content updates, page embeds, images, speed and mobile experience."),
                ("Search", "Google Search Console and SEO basics so the site stays visible."),
                ("Security", "Security hardening across every system (June 2026): logins, secrets, limits and headers."),
                ("Railway security incident", "In October 2026 our hosting provider had a breach that exposed the keys our systems use. I checked every account for misuse "
                 "(none found) and have been replacing the keys across all 28 systems, starting with Stripe and the AI keys."),
                ("Email accounts", "Setting up and managing all Physique Academy email accounts."),
                ("Domains", "Our domains and DNS, and the subdomains every dashboard lives on."),
            ]),
        ],
    },
    {
        "id": "design", "eyebrow": "Section 11", "title": "Graphic design",
        "blocks": [
            ("bullets", [
                ("Brand", "Keeping everything consistent with the PA brand."),
                ("Ads and social", "Graphics and ad creatives for Meta."),
                ("Client resources", "Workout plans, guides and booklets, including the Lean Bulk and No BS Fat Loss blueprints."),
                ("Business documents", "Internal and client-facing documents in PA branding."),
            ]),
        ],
    },
    {
        "id": "clothing", "eyebrow": "Section 12", "title": "Clothing, merchandise and fulfilment",
        "blocks": [
            ("bullets", [
                ("Client apparel", "Welcome merch for new clients, hoodies at 6 months, and merch whenever the team asks."),
                ("Stock", "Ordering, holding and managing stock levels."),
                ("Despatch", "Picking, packing and sending orders, and dealing with couriers."),
                ("Fulfilment provider", "Reviewed the options against a full cost model, negotiated terms and am managing the move to the new provider."),
                ("Shopify", "Products, stock, shipping rates and checkout."),
                ("Design", "Print designs and mock-ups for new items."),
            ]),
        ],
    },
    {
        "id": "admin", "eyebrow": "Section 13", "title": "Company admin",
        "blocks": [
            ("bullets", [
                ("US company", "Set up and run Physique Coaching LLC (Wyoming), its EIN and Mercury bank account, so we can take US payments properly."),
                ("Apple Developer", "Enrolment for Physique Academy LTD."),
                ("Suppliers and subscriptions", "Own the accounts and renewals for the platforms in Section 5 and keep the spend in line with what we get from them."),
            ]),
        ],
    },
    {
        "id": "team", "eyebrow": "Section 14", "title": "Team and communication",
        "blocks": [
            ("bullets", [
                ("Marketing meeting", "Weekly Tuesday marketing meeting."),
                ("Daniel Bentham", "Weekly call on site stats, ad creative and Meta."),
                ("Working with you", "Priorities, scheduling and bringing the numbers into decisions."),
                ("Advising", "Where a decision depends on what the numbers say, or what a system can and can't do, I give you the real picture."),
            ]),
        ],
    },
    {
        "id": "next", "eyebrow": "Section 15", "title": "In progress and coming up",
        "blocks": [
            ("h3", "In progress now"),
            ("bullets", [
                ("Finish replacing keys", "Working through the remaining keys after the hosting provider's breach."),
                ("ActiveCampaign switch-off", "Move the last booked-call emails to Klaviyo or GoHighLevel so ActiveCampaign doesn't need renewing."),
                ("UK to US Stripe moves", "Finishing client moves once they've signed up on the new link."),
                ("Welcome Tee", "Built and testing; waiting on answers from the warehouse."),
                ("US call coverage", "Covering the 2pm to 7pm US Eastern gap and setting Patrick's hours (your call)."),
                ("US phone number", "A US number in GoHighLevel for the sales team's US calls."),
            ]),
            ("h3", "Ready to start when you give the go-ahead"),
            ("bullets", [
                ("Replace ChartMogul", "Our own client and revenue tracking from Stripe, saving $550 a month."),
                ("Website standby copy", "A ready-to-go copy of physiqueacademy.com in case the website agency's hosting goes down."),
            ]),
            ("h3", "Planned"),
            ("bullets", [
                ("Owner's overview", "Adding live numbers (sales, bookings, client numbers, at-risk clients) to the Command Center."),
                ("Churn early warning", "An at-risk panel per coach combining failed payments, upcoming cancellations and payment history."),
                ("Cancellation save flow", "Offering a pause or downgrade before a cancellation goes through, and tracking how many we save."),
                ("Failed-payment recovery", "Sending clients a secure link to update their card the moment a payment fails, with follow-ups."),
                ("Renewals on the coach dashboard", "Flagging clients near the end of their term so the renewal conversation starts in time."),
                ("Weekly coach digest", "A Monday message to each coach with their new and lost clients and anyone needing attention."),
                ("Client history view", "Click a client in Coach Hub to see their full history in one place."),
                ("Coach testimonials", "Each coach's testimonials and transformations on their dashboard."),
                ("Coach Hub help", "Written and video guides for everything on the Hub."),
            ]),
        ],
    },
]
