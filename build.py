#!/usr/bin/env python3
"""Generates the static site (EN at /, ES at /es/) into this folder. Run: python3 build.py

All copy lives in the T dict below; style.css is shared. Nothing here needs a server — the output is
plain HTML for GitHub Pages (or any static host).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://freedompoint.app"
EMAIL = "FreedomPointApp@gmail.com"
# Replace with the real App Store link when the app is live; while it is None the buttons say "coming soon".
APP_STORE_URL = None
UPDATED = {"en": "November 23, 2026", "es": "23 de noviembre de 2026"}

# Page paths per language: (index, privacy, support)
PATHS = {
    "en": {"index": "/", "privacy": "/privacy.html", "support": "/support.html"},
    "es": {"index": "/es/", "privacy": "/es/privacidad.html", "support": "/es/soporte.html"},
}
FILES = {
    "en": {"index": "index.html", "privacy": "privacy.html", "support": "support.html"},
    "es": {"index": "es/index.html", "privacy": "es/privacidad.html", "support": "es/soporte.html"},
}

T = {
    "en": {
        "lang": "en",
        "nav_features": "Features", "nav_about": "About", "nav_support": "Support",
        "home_label": "FreedomPoint home",
        "title": "FreedomPoint: Net Worth & Financial Freedom Planner for iPhone",
        "desc": "See your whole net worth in one number and how far you are from financial freedom. Brokerage, RSUs, cash and property in one iPhone app. No account, no ads, no tracking.",
        "og": "Know exactly how far you are from financial freedom.",
        "hero_label": "Net worth and financial freedom, on iPhone",
        "hero_h1": "Know exactly how far you are from freedom.",
        "hero_lead": "Your brokerage, RSUs, cash and property become one number. Then FreedomPoint shows the capital you need, the date you can reach it and the plan to get there.",
        "cta": "Coming soon to the App Store",
        "cta_close": "Coming soon to the App Store",
        "cta_fine": "No account. No ads. No tracking.",
        "bands": [
            {
                "label": "Net worth", "h2": "Everything you own, in one number.",
                "lead": "Brokerage, RSUs, cash, real estate and everything else, added up in the currency you choose and tracked over time. Tap a category to see what is inside it.",
                "pts": [
                    "Holdings in other currencies are converted for you",
                    "Bring your data in from Excel, or type it in by hand",
                    "A chart of how your net worth has moved, so the trend is as visible as the total",
                ],
                "img": "networth", "alt": "FreedomPoint net worth screen with the total and its breakdown by category",
            },
            {
                "label": "Stock Market", "h2": "Your positions, live.",
                "lead": "Quotes for everything you hold in your brokerage and RSU accounts, with realized and unrealized gains, returns by period and the vesting date of every RSU lot.",
                "pts": [
                    "Gains and losses by position and in total, for the period you pick",
                    "Year to date, month to date or any other window",
                    "Optional AI summaries of the news and fundamentals behind each ticker",
                ],
                "img": "stock", "alt": "Stock Market screen with positions, daily and period gains",
            },
            {
                "label": "Freedom Point", "h2": "Your date. Your number.",
                "lead": "Say how much yearly income you want, when, and for how long. FreedomPoint works out the capital that takes, and builds a year-by-year savings and investment plan around your risk profile.",
                "pts": [
                    "Capital needed, and how much of it you already have",
                    "A plan that follows the risk profile you choose, with concrete funds to put money into",
                    "See how far your real portfolio drifts from the plan",
                ],
                "img": "freedompoint", "alt": "Freedom Point screen showing the capital needed and progress toward it",
            },
            {
                "label": "Flash", "h2": "Where you stand, in a glance.",
                "lead": "Open the app on Flash: your net worth, this year's goal, the stock market year to date and how short you are of your Freedom Point. One screen, no digging.",
                "pts": [
                    "Your yearly goal, with how far ahead or behind you are",
                    "Stock Market year to date, straight from your own positions",
                    "Light and dark, in English and Spanish",
                ],
                "img": "flash", "alt": "Flash screen with net worth, yearly goal, stock market year to date and distance to the Freedom Point",
            },
        ],
        "more_label": "And more", "more_h2": "The rest of the toolbox.",
        "more_lead": "Everything is built around one question: are you on track, and what should you do next?",
        "cards": [
            ("Rebalance", "Set the mix you want across categories and see exactly how much to buy or sell to get back to it."),
            ("Risk profile", "A short questionnaire sets a Conservative, Moderate or Aggressive profile that shapes your plan."),
            ("Stock analysis", "Fundamentals, analyst consensus and news per ticker, written by the AI provider you choose."),
            ("Share with your partner", "Share one portfolio between your devices, or with a person you invite, through iCloud."),
        ],
        "about_label": "About", "about_h2": "Built to answer one question.",
        "about_p": [
            "FreedomPoint is made by an independent developer who wanted one honest answer to “how far am I from financial freedom?” without handing account credentials to anyone.",
            "That is why there is no bank login: you bring in your own numbers, and they stay on your devices and in your own iCloud.",
            "Your ideas shape it. Tell us what you wish your plan could do, and the next update might be yours.",
        ],
        "about_cta": "Send us a suggestion", "about_subject": "FreedomPoint suggestion",
        "faq_label": "FAQ", "faq_h2": "Questions people ask.",
        "faq": [
            ("Do I need an account?", "No. FreedomPoint has no accounts and no server of its own. Open it and start. Your data lives on your iPhone and, if you have iCloud turned on, in your own private iCloud so your devices stay in sync."),
            ("Does it connect to my bank or broker?", "No, and it never asks for your credentials. You enter your holdings by hand or import them from an Excel file, so you stay in control of what the app knows."),
            ("Can you see my financial data?", "No. Your portfolio is stored in your private iCloud database, which the developer has no access to. There is no analytics and no tracking in the app. The privacy policy lists every case where anything leaves your device."),
            ("Where do the quotes come from?", "From Yahoo Finance. The app sends the ticker symbols (and currency pairs for conversion) to fetch prices. Prices can be delayed or unavailable, so treat them as informative, not as a trading feed."),
            ("What do the AI features do, and what do they cost?", "AI suggestions, news summaries and stock analysis are optional. You choose Anthropic (Claude) or Google Gemini and add your own API key, which stays in your device's Keychain. Usage is billed by that provider, not by us. The privacy policy explains exactly what each feature sends."),
            ("Is this financial advice?", "No. FreedomPoint is a tracking and planning tool. Projections are estimates built on the assumptions you set, and the plan and AI suggestions are not investment, tax or legal advice. Past returns do not guarantee future ones."),
            ("Which languages and currencies are supported?", "The app is in English and Spanish, independent of your phone’s language. You pick the currency your net worth is shown in, and holdings in other currencies are converted."),
        ],
        "strip": [
            ("No account", "Open the app and start. Nothing to sign up for."),
            ("Private by design", "No analytics, no ads, no tracking, no server of ours."),
            ("Your iCloud, not ours", "Synced through your own iCloud, never through us."),
            ("You decide what it knows", "Type it in or import it. No bank login, ever."),
        ],
        "close_h2": "Your freedom has a date. Find it.",
        "close_lead": "Start with the numbers you already have.",
        "footer_support": "Support", "footer_privacy": "Privacy",
        "footer_note": "FreedomPoint is a tracking and planning tool. It is not financial, tax or investment advice, and projections are estimates.",
        "footer_tm": "Not affiliated with Apple, Yahoo, Anthropic or Google. All trademarks belong to their owners.",
        "copyright": "© 2026 FreedomPoint. All rights reserved.",
        "ld_desc": "See your whole net worth in one number and how far you are from financial freedom: brokerage, RSUs, cash and property in one iPhone app.",
        # support
        "sup_title": "FreedomPoint Support", "sup_desc": "Support for the FreedomPoint net worth and financial freedom app.",
        "sup_eyebrow": "Support", "sup_h1": "FreedomPoint Support", "sup_sub": "Help with FreedomPoint for iPhone.",
        "sup_contact": f"Questions, bug reports or feedback: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>. Please include your iOS version and, if you can, what you were doing when the problem happened. We aim to reply within a few days.",
        "sup_faq_h2": "Frequently asked questions",
        "sup_faq": [
            ("Where is my data stored?", "On your device, and in your own private iCloud if iCloud is on, so your devices stay in sync. FreedomPoint has no account system and no server of its own. See the <a href=\"{privacy}\">privacy policy</a>."),
            ("My quotes are not updating.", "Pull down on a screen to refresh. Quotes come from Yahoo Finance and can be delayed or temporarily unavailable. Check your connection and try again in a few minutes."),
            ("How do I import from Excel?", "Open the More menu › Settings, and under the Excel section choose your workbook. The Broker, RSU and other-asset sheets are read on your device. Nothing is uploaded."),
            ("How do the AI features work?", "They are optional. In Settings you pick Anthropic (Claude) or Google Gemini and paste your own API key. The key stays in your device’s Keychain. See the <a href=\"{privacy}\">privacy policy</a> for what each feature sends."),
            ("How do I share my portfolio with my partner?", "In Settings, use the sharing section to invite them through iCloud. They need an iCloud account and the app installed. You can stop sharing at any time."),
            ("How do I delete my data?", "Delete the app to remove the data stored on the device. To remove the copy in iCloud, open Settings › your name › iCloud › Manage Account Storage › FreedomPoint and delete its data."),
        ],
        "sup_foot": "FreedomPoint, a personal net worth and planning app.",
        # privacy
        "pri_title": "FreedomPoint Privacy Policy", "pri_desc": "Privacy policy for the FreedomPoint app: what stays on your device and the few cases where data leaves it.",
        "pri_eyebrow": "Privacy Policy", "pri_h1": "FreedomPoint keeps your finances yours.",
        "pri_sub": "Last updated {updated} · Applies to FreedomPoint for iOS, version 1.0",
    },
    "es": {
        "lang": "es",
        "nav_features": "Funciones", "nav_about": "Acerca de", "nav_support": "Soporte",
        "home_label": "Inicio de FreedomPoint",
        "title": "FreedomPoint: patrimonio y libertad financiera para iPhone",
        "desc": "Ve todo tu patrimonio en un solo número y qué tan lejos estás de la libertad financiera. Broker, RSU, efectivo e inmuebles en una app para iPhone. Sin cuenta, sin anuncios, sin rastreo.",
        "og": "Sabe exactamente qué tan lejos estás de la libertad financiera.",
        "hero_label": "Patrimonio y libertad financiera, en iPhone",
        "hero_h1": "Sabe exactamente qué tan lejos estás de tu libertad.",
        "hero_lead": "Tu broker, tus RSU, tu efectivo y tus inmuebles se vuelven un solo número. Después FreedomPoint te muestra el capital que necesitas, la fecha en que puedes alcanzarlo y el plan para lograrlo.",
        "cta": "Próximamente en el App Store",
        "cta_close": "Próximamente en el App Store",
        "cta_fine": "Sin cuenta. Sin anuncios. Sin rastreo.",
        "bands": [
            {
                "label": "Patrimonio", "h2": "Todo lo que tienes, en un solo número.",
                "lead": "Broker, RSU, efectivo, inmuebles y todo lo demás, sumado en la moneda que elijas y seguido en el tiempo. Toca una categoría para ver qué hay dentro.",
                "pts": [
                    "Lo que tienes en otras monedas se convierte por ti",
                    "Trae tus datos desde Excel o cárgalos a mano",
                    "Una gráfica de cómo se ha movido tu patrimonio, para ver la tendencia y no solo el total",
                ],
                "img": "networth", "alt": "Pantalla de Patrimonio de FreedomPoint con el total y su desglose por categoría",
            },
            {
                "label": "Stock Market", "h2": "Tus posiciones, en vivo.",
                "lead": "Cotizaciones de todo lo que tienes en tu broker y tus RSU, con ganancias realizadas y no realizadas, rendimientos por periodo y la fecha de vesting de cada lote de RSU.",
                "pts": [
                    "Ganancias y pérdidas por posición y en total, del periodo que elijas",
                    "Lo que va del año, del mes o cualquier otra ventana",
                    "Resúmenes opcionales con IA de las noticias y los fundamentales de cada ticker",
                ],
                "img": "stock", "alt": "Pantalla de Stock Market con posiciones y ganancias diarias y por periodo",
            },
            {
                "label": "Freedom Point", "h2": "Tu fecha. Tu número.",
                "lead": "Dices cuánto ingreso anual quieres, para cuándo y por cuánto tiempo. FreedomPoint calcula el capital que eso requiere y arma un plan de ahorro e inversión año por año según tu perfil de riesgo.",
                "pts": [
                    "El capital necesario y cuánto de él ya tienes",
                    "Un plan que sigue el perfil de riesgo que elijas, con fondos concretos donde invertir",
                    "Cuánto se desvía tu portafolio real del plan",
                ],
                "img": "freedompoint", "alt": "Pantalla de Freedom Point con el capital necesario y el avance hacia él",
            },
            {
                "label": "Flash", "h2": "Dónde estás, de un vistazo.",
                "lead": "Abre la app en Flash: tu patrimonio, la meta del año, el mercado de acciones en lo que va del año y cuánto te falta para tu Freedom Point. Una sola pantalla, sin buscar.",
                "pts": [
                    "Tu meta anual, con cuánto vas por delante o por detrás",
                    "Stock Market en lo que va del año, directo de tus propias posiciones",
                    "Modo claro y oscuro, en español e inglés",
                ],
                "img": "flash", "alt": "Pantalla Flash con patrimonio, meta anual, mercado en el año y distancia al Freedom Point",
            },
        ],
        "more_label": "Y más", "more_h2": "El resto de la caja de herramientas.",
        "more_lead": "Todo gira alrededor de una pregunta: ¿vas bien encaminado y qué sigue?",
        "cards": [
            ("Rebalanceo", "Define la mezcla que quieres por categoría y mira exactamente cuánto comprar o vender para volver a ella."),
            ("Perfil de riesgo", "Un cuestionario corto define un perfil Conservador, Moderado o Agresivo que da forma a tu plan."),
            ("Análisis de acciones", "Fundamentales, consenso de analistas y noticias por ticker, escritos por el proveedor de IA que elijas."),
            ("Comparte con tu pareja", "Comparte un mismo portafolio entre tus dispositivos o con una persona que invites, a través de iCloud."),
        ],
        "about_label": "Acerca de", "about_h2": "Hecha para responder una pregunta.",
        "about_p": [
            "FreedomPoint la hace un desarrollador independiente que quería una respuesta honesta a «¿qué tan lejos estoy de la libertad financiera?» sin darle sus credenciales bancarias a nadie.",
            "Por eso no hay inicio de sesión con tu banco: tú traes tus propias cifras y se quedan en tus dispositivos y en tu propio iCloud.",
            "Tus ideas le dan forma. Cuéntanos qué te gustaría que hiciera tu plan y la próxima actualización podría ser la tuya.",
        ],
        "about_cta": "Envíanos una sugerencia", "about_subject": "Sugerencia para FreedomPoint",
        "faq_label": "Preguntas frecuentes", "faq_h2": "Lo que la gente pregunta.",
        "faq": [
            ("¿Necesito una cuenta?", "No. FreedomPoint no tiene cuentas ni un servidor propio. Ábrela y empieza. Tus datos viven en tu iPhone y, si tienes iCloud activado, en tu propio iCloud privado para que tus dispositivos queden sincronizados."),
            ("¿Se conecta con mi banco o mi broker?", "No, y nunca te pide tus credenciales. Cargas tus posiciones a mano o las importas desde un archivo de Excel, así tú controlas lo que la app sabe."),
            ("¿Pueden ver mis datos financieros?", "No. Tu portafolio se guarda en tu base de datos privada de iCloud, a la que el desarrollador no tiene acceso. La app no tiene analítica ni rastreo. La política de privacidad enumera cada caso en que algo sale de tu dispositivo."),
            ("¿De dónde salen las cotizaciones?", "De Yahoo Finance. La app envía los símbolos (y los pares de monedas para la conversión) para obtener precios. Los precios pueden llegar con retraso o no estar disponibles, así que trátalos como informativos, no como un feed para operar."),
            ("¿Qué hacen las funciones de IA y cuánto cuestan?", "Las sugerencias, los resúmenes de noticias y el análisis de acciones con IA son opcionales. Tú eliges Anthropic (Claude) o Google Gemini y agregas tu propia clave de API, que queda en el Llavero de tu dispositivo. El uso lo cobra ese proveedor, no nosotros. La política de privacidad explica exactamente qué envía cada función."),
            ("¿Esto es asesoría financiera?", "No. FreedomPoint es una herramienta de seguimiento y planeación. Las proyecciones son estimaciones basadas en los supuestos que tú defines, y el plan y las sugerencias con IA no son asesoría de inversión, fiscal ni legal. Los rendimientos pasados no garantizan los futuros."),
            ("¿Qué idiomas y monedas admite?", "La app está en español e inglés, independientemente del idioma de tu teléfono. Tú eliges la moneda en que ver tu patrimonio y lo que tienes en otras monedas se convierte."),
        ],
        "strip": [
            ("Sin cuenta", "Abre la app y empieza. No hay nada que registrar."),
            ("Privada por diseño", "Sin analítica, sin anuncios, sin rastreo, sin servidor nuestro."),
            ("Tu iCloud, no el nuestro", "Se sincroniza con tu propio iCloud, nunca con nosotros."),
            ("Tú decides qué sabe", "Escríbelo o impórtalo. Nunca un inicio de sesión bancario."),
        ],
        "close_h2": "Tu libertad tiene fecha. Encuéntrala.",
        "close_lead": "Empieza con los números que ya tienes.",
        "footer_support": "Soporte", "footer_privacy": "Privacidad",
        "footer_note": "FreedomPoint es una herramienta de seguimiento y planeación. No es asesoría financiera, fiscal ni de inversión, y las proyecciones son estimaciones.",
        "footer_tm": "Sin afiliación con Apple, Yahoo, Anthropic ni Google. Todas las marcas pertenecen a sus dueños.",
        "copyright": "© 2026 FreedomPoint. Todos los derechos reservados.",
        "ld_desc": "Ve todo tu patrimonio en un solo número y qué tan lejos estás de la libertad financiera: broker, RSU, efectivo e inmuebles en una app para iPhone.",
        "sup_title": "Soporte de FreedomPoint", "sup_desc": "Soporte de la app de patrimonio y libertad financiera FreedomPoint.",
        "sup_eyebrow": "Soporte", "sup_h1": "Soporte de FreedomPoint", "sup_sub": "Ayuda con FreedomPoint para iPhone.",
        "sup_contact": f"Preguntas, reportes de errores o comentarios: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>. Incluye tu versión de iOS y, si puedes, qué estabas haciendo cuando ocurrió el problema. Buscamos responder en unos días.",
        "sup_faq_h2": "Preguntas frecuentes",
        "sup_faq": [
            ("¿Dónde se guardan mis datos?", "En tu dispositivo y, si iCloud está activado, en tu propio iCloud privado para que tus dispositivos queden sincronizados. FreedomPoint no tiene sistema de cuentas ni servidor propio. Consulta la <a href=\"{privacy}\">política de privacidad</a>."),
            ("Mis cotizaciones no se actualizan.", "Desliza hacia abajo en una pantalla para actualizar. Las cotizaciones vienen de Yahoo Finance y pueden llegar con retraso o no estar disponibles por un rato. Revisa tu conexión e inténtalo de nuevo en unos minutos."),
            ("¿Cómo importo desde Excel?", "Abre el menú Más › Ajustes y, en la sección de Excel, elige tu libro. Las hojas de Broker, RSU y otros activos se leen en tu dispositivo. No se sube nada."),
            ("¿Cómo funcionan las funciones de IA?", "Son opcionales. En Ajustes eliges Anthropic (Claude) o Google Gemini y pegas tu propia clave de API. La clave queda en el Llavero de tu dispositivo. Consulta la <a href=\"{privacy}\">política de privacidad</a> para ver qué envía cada función."),
            ("¿Cómo comparto mi portafolio con mi pareja?", "En Ajustes, usa la sección de compartir para invitarla por iCloud. Necesita una cuenta de iCloud y la app instalada. Puedes dejar de compartir cuando quieras."),
            ("¿Cómo borro mis datos?", "Elimina la app para borrar los datos guardados en el dispositivo. Para quitar la copia en iCloud, abre Ajustes › tu nombre › iCloud › Administrar almacenamiento › FreedomPoint y borra sus datos."),
        ],
        "sup_foot": "FreedomPoint, una app personal de patrimonio y planeación.",
        "pri_title": "Política de privacidad de FreedomPoint", "pri_desc": "Política de privacidad de la app FreedomPoint: qué se queda en tu dispositivo y los pocos casos en que los datos salen de él.",
        "pri_eyebrow": "Política de privacidad", "pri_h1": "FreedomPoint mantiene tus finanzas en tus manos.",
        "pri_sub": "Última actualización: {updated} · Aplica a FreedomPoint para iOS, versión 1.0",
    },
}

# ---------------------------------------------------------------- privacy page body (per language)
PRIVACY = {
    "en": {
        "box": [
            "FreedomPoint is a net worth and financial planning app. It has no account system, no server of its own and no analytics. Your portfolio is stored on your iPhone and, if you use iCloud, in your own private iCloud database.",
            "We do not sell, rent or share your data, and we never receive it: the developer has no access to your private iCloud data. A few features reach out to the internet on purpose, and they are all listed on this page with exactly what they send.",
        ],
        "pills": ["No account required", "No developer server", "No analytics or tracking", "No ads", "Portfolio synced through your own iCloud"],
        "stores_h2": "What FreedomPoint stores, and why",
        "stores_th": ("Data", "Where it comes from", "Why it is kept"),
        "stores": [
            ("Holdings and transactions", "What you type in, or import from an Excel file", "They are the portfolio: tickers, quantities, purchase dates and prices, and the values of cash, property and other assets."),
            ("Plan and goals", "The income, date, duration, risk answers and targets you set", "To calculate your Freedom Point, your yearly goal and your plan."),
            ("Country of residence and of each asset", "Chosen by you in Settings and on each asset", "Stored on your device so the app can describe your holdings by location. The country of an asset is saved with the asset."),
            ("Net worth history", "Snapshots the app takes of your totals", "To draw the evolution chart."),
            ("Preferences", "Currency, language, AI provider and similar choices", "So the app remembers your settings between launches."),
            ("API keys you add", "Pasted by you in Settings", "To call the AI provider you chose. Kept in the device Keychain, on that device only. They are not synced to iCloud."),
        ],
        "sections": [
            ("iCloud sync and sharing",
             ["If iCloud is on, FreedomPoint syncs your portfolio between your devices through Apple’s CloudKit, into your own private database. Apple processes that data under its own privacy policy. The developer cannot read it.",
              "If you invite another person to a shared portfolio, they see what you share and can only do what the invitation allows. You can stop sharing at any time from the app."]),
            ("Quotes and exchange rates",
             ["To show prices, FreedomPoint requests data from Yahoo Finance. Each request contains the ticker symbol (for example a stock or fund symbol) or a currency pair (for example EURUSD) and, like any internet request, reaches Yahoo with your device’s IP address.",
              "No amounts, quantities, names or account information are sent. Yahoo handles those requests under its own privacy policy, and FreedomPoint does not receive or store it. Prices can be delayed or unavailable."]),
            ("Plan assumptions (public file)",
             ["The savings plan uses long-term return estimates published by J.P. Morgan Asset Management. To keep them current, FreedomPoint downloads a public file from freedompoint.app/assumptions/v1.json at most once a week. It is a plain download: the request contains nothing about you or your portfolio and, like any internet request, reaches the host of this website (GitHub Pages) with your device’s IP address. The developer does not receive or store these requests.",
              "If the download fails, the app keeps using the figures built into it. Every figure, with the publications behind it and how it was calculated, is shown in the app under “Where these numbers come from”."]),
            ("AI features (optional)",
             ["AI features run only if you pick a provider (Anthropic or Google Gemini) in Settings and add your own API key. Requests go from your device straight to that provider; they do not pass through any server of ours. Your use is governed by the provider’s own terms and privacy policy, and billed by them.",
              "What each feature sends:"]),
        ],
        "ai_list": [
            "<b>News, fundamentals, moat, legal and analyst summaries, and dividend estimates:</b> only the ticker symbol you are looking at.",
            "<b>Portfolio suggestions:</b> your total net worth, your goal amount (if you set one) and, for each category, your current share, your target share and the amount to buy or sell to reach it. Holdings, tickers, names, notes and photos are not sent.",
            "<b>The Flash screen’s news card</b> currently shows placeholder examples and sends nothing anywhere.",
        ],
        "after_ai": "Use these features only if you are comfortable with the above. Everything else in the app works without them.",
        "sections2": [
            ("Excel import and export",
             ["When you import a workbook, the file is read on your device and nothing is uploaded. Anything you export is a file you control; FreedomPoint does not send a copy anywhere."]),
            ("Notifications and background activity",
             ["FreedomPoint does not send you notifications. It uses silent system pushes only so that iCloud can tell your devices that data changed."]),
            ("What we do not do",
             ["We do not ask for your bank or broker credentials, we do not connect to financial institutions, we do not include advertising or analytics, we do not track you across apps or websites and we do not build a profile of you."]),
            ("If you export or delete your data",
             ["Deleting the app deletes the data stored on the device. The copy in your private iCloud is removed from Settings › your name › iCloud › Manage Account Storage › FreedomPoint. There is no account to close and no server-side copy with us to request deletion of, because none exists."]),
            ("Children’s privacy",
             ["FreedomPoint is a personal finance app and is not directed at children. We do not collect data about any user, adult or minor."]),
            ("Changes to this policy",
             ["If FreedomPoint adds a feature that changes what is described here, for example a new data service, this page will be updated first, with the date above reflecting the change, before that feature ships."]),
        ],
        "contact_h2": "Contact", "contact_p": "Questions about this policy or FreedomPoint:",
    },
    "es": {
        "box": [
            "FreedomPoint es una app de patrimonio y planeación financiera. No tiene sistema de cuentas, servidor propio ni analítica. Tu portafolio se guarda en tu iPhone y, si usas iCloud, en tu propia base de datos privada de iCloud.",
            "No vendemos, rentamos ni compartimos tus datos, y nunca los recibimos: el desarrollador no tiene acceso a tus datos privados de iCloud. Unas pocas funciones se conectan a internet a propósito, y todas están listadas en esta página con lo que envían exactamente.",
        ],
        "pills": ["No requiere cuenta", "Sin servidor del desarrollador", "Sin analítica ni rastreo", "Sin anuncios", "Portafolio sincronizado con tu propio iCloud"],
        "stores_h2": "Qué guarda FreedomPoint y por qué",
        "stores_th": ("Dato", "De dónde viene", "Por qué se guarda"),
        "stores": [
            ("Posiciones y transacciones", "Lo que escribes o importas desde un archivo de Excel", "Son el portafolio: tickers, cantidades, fechas y precios de compra, y los valores de efectivo, inmuebles y otros activos."),
            ("Plan y metas", "El ingreso, la fecha, la duración, las respuestas de riesgo y los objetivos que defines", "Para calcular tu Freedom Point, tu meta anual y tu plan."),
            ("País de residencia y de cada activo", "Lo eliges tú en Ajustes y en cada activo", "Se guarda en tu dispositivo para que la app describa tus tenencias por ubicación. El país de un activo se guarda junto con el activo."),
            ("Historial de patrimonio", "Instantáneas que la app toma de tus totales", "Para dibujar la gráfica de evolución."),
            ("Preferencias", "Moneda, idioma, proveedor de IA y opciones similares", "Para que la app recuerde tus ajustes entre aperturas."),
            ("Claves de API que agregas", "Las pegas tú en Ajustes", "Para llamar al proveedor de IA que elegiste. Se guardan en el Llavero del dispositivo, solo en ese dispositivo. No se sincronizan con iCloud."),
        ],
        "sections": [
            ("Sincronización con iCloud y compartir",
             ["Si iCloud está activado, FreedomPoint sincroniza tu portafolio entre tus dispositivos mediante CloudKit de Apple, en tu propia base de datos privada. Apple procesa esos datos según su propia política de privacidad. El desarrollador no puede leerlos.",
              "Si invitas a otra persona a un portafolio compartido, verá lo que compartas y solo podrá hacer lo que permita la invitación. Puedes dejar de compartir cuando quieras desde la app."]),
            ("Cotizaciones y tipos de cambio",
             ["Para mostrar precios, FreedomPoint solicita datos a Yahoo Finance. Cada solicitud contiene el símbolo del ticker (por ejemplo el de una acción o un fondo) o un par de monedas (por ejemplo EURUSD) y, como cualquier solicitud a internet, llega a Yahoo con la dirección IP de tu dispositivo.",
              "No se envían montos, cantidades, nombres ni información de cuentas. Yahoo trata esas solicitudes según su propia política de privacidad, y FreedomPoint no la recibe ni la guarda. Los precios pueden llegar con retraso o no estar disponibles."]),
            ("Supuestos del plan (archivo público)",
             ["El plan de ahorro usa estimaciones de rendimiento a largo plazo que publica J.P. Morgan Asset Management. Para mantenerlas al día, FreedomPoint descarga un archivo público desde freedompoint.app/assumptions/v1.json como máximo una vez por semana. Es una descarga simple: la solicitud no contiene nada sobre ti ni sobre tu portafolio y, como cualquier solicitud de internet, llega al servidor que aloja este sitio (GitHub Pages) con la dirección IP de tu dispositivo. El desarrollador no recibe ni guarda esas solicitudes.",
              "Si la descarga falla, la app sigue usando los valores incluidos en ella. Cada cifra, con las publicaciones en las que se basa y cómo se calculó, se muestra en la app en “De dónde salen estos números”."]),
            ("Funciones de IA (opcionales)",
             ["Las funciones de IA solo operan si eliges un proveedor (Anthropic o Google Gemini) en Ajustes y agregas tu propia clave de API. Las solicitudes van de tu dispositivo directo a ese proveedor; no pasan por ningún servidor nuestro. Tu uso se rige por los términos y la política de privacidad del proveedor, y él te lo cobra.",
              "Qué envía cada función:"]),
        ],
        "ai_list": [
            "<b>Noticias, fundamentales, foso competitivo, temas legales, comentarios de analistas y estimación de dividendos:</b> solo el símbolo del ticker que estás viendo.",
            "<b>Sugerencias de portafolio:</b> tu patrimonio total, el monto de tu meta (si definiste una) y, por categoría, tu porcentaje actual, tu porcentaje objetivo y el monto a comprar o vender para llegar a él. No se envían posiciones, tickers, nombres, notas ni fotos.",
            "<b>La tarjeta de noticias de la pantalla Flash</b> hoy muestra ejemplos de relleno y no envía nada a ningún lado.",
        ],
        "after_ai": "Usa estas funciones solo si estás de acuerdo con lo anterior. Todo lo demás de la app funciona sin ellas.",
        "sections2": [
            ("Importar y exportar Excel",
             ["Al importar un libro, el archivo se lee en tu dispositivo y no se sube nada. Lo que exportes es un archivo que tú controlas; FreedomPoint no envía una copia a ningún lado."]),
            ("Notificaciones y actividad en segundo plano",
             ["FreedomPoint no te envía notificaciones. Usa notificaciones silenciosas del sistema solo para que iCloud avise a tus dispositivos que hubo cambios."]),
            ("Lo que no hacemos",
             ["No pedimos tus credenciales del banco o del broker, no nos conectamos a instituciones financieras, no incluimos publicidad ni analítica, no te rastreamos entre apps o sitios web y no armamos un perfil tuyo."]),
            ("Si exportas o borras tus datos",
             ["Eliminar la app borra los datos guardados en el dispositivo. La copia en tu iCloud privado se elimina desde Ajustes › tu nombre › iCloud › Administrar almacenamiento › FreedomPoint. No hay una cuenta que cerrar ni una copia en nuestros servidores cuya eliminación solicitar, porque no existe."]),
            ("Privacidad de menores",
             ["FreedomPoint es una app de finanzas personales y no está dirigida a menores. No recopilamos datos de ningún usuario, adulto o menor."]),
            ("Cambios a esta política",
             ["Si FreedomPoint agrega una función que cambie lo descrito aquí, por ejemplo un nuevo servicio de datos, esta página se actualizará primero, con la fecha de arriba reflejando el cambio, antes de que esa función salga."]),
        ],
        "contact_h2": "Contacto", "contact_p": "Preguntas sobre esta política o sobre FreedomPoint:",
    },
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def head(lang, kind, title, desc, extra=""):
    t = T[lang]
    other = "es" if lang == "en" else "en"
    url = SITE + PATHS[lang][kind]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#f1efe8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121514" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="{lang}" href="{url}">
<link rel="alternate" hreflang="{other}" href="{SITE + PATHS[other][kind]}">
<link rel="alternate" hreflang="x-default" href="{SITE + PATHS['en'][kind]}">
<link rel="icon" href="/img/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(t['og'])}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Sora:wght@500;600;700&display=swap">
<link rel="stylesheet" href="/style.css">
{extra}</head>
"""


def nav(lang, kind):
    t = T[lang]
    p = PATHS[lang]
    en_href, es_href = PATHS["en"][kind], PATHS["es"][kind]
    feats = f'<a class="hide-sm" href="{p["index"]}#features">{t["nav_features"]}</a>' if kind == "index" else ""
    about = f'<a class="hide-sm" href="{p["index"]}#about">{t["nav_about"]}</a>'
    return f"""<body>
<div class="in">
  <nav>
    <a class="brand" href="{p['index']}" aria-label="{t['home_label']}"><picture><source media="(prefers-color-scheme: dark)" srcset="/img/freedompoint-lockup-dark.svg"><img src="/img/freedompoint-lockup-light.svg" alt="FreedomPoint" width="150" height="30"></picture></a>
    <span class="navlinks">{feats}{about}<a href="{p['support']}">{t['nav_support']}</a><span class="lang" role="group" aria-label="Language"><a href="{en_href}" lang="en" hreflang="en"{' aria-current="true"' if lang == 'en' else ''}>EN</a><a href="{es_href}" lang="es" hreflang="es"{' aria-current="true"' if lang == 'es' else ''}>ES</a></span></span>
  </nav>
"""


def footer(lang):
    t = T[lang]
    p = PATHS[lang]
    return f"""  <footer>
    <a href="{p['support']}">{t['footer_support']}</a><a href="{p['privacy']}">{t['footer_privacy']}</a>
    <span>{t['footer_note']}</span>
    <span>{t['footer_tm']}</span>
    <span>{t['copyright']}</span>
  </footer>
</div>
</body>
</html>
"""


def cta(lang, key="cta"):
    t = T[lang]
    if APP_STORE_URL:
        label = "Download on the App Store" if lang == "en" else "Descargar en el App Store"
        return f'<a class="cta" href="{APP_STORE_URL}">{label}</a>'
    return f'<span class="cta soon" role="note">{t[key]}</span>'


def index(lang):
    t = T[lang]
    p = PATHS[lang]
    ld_app = {
        "@context": "https://schema.org", "@type": "MobileApplication", "name": "FreedomPoint",
        "operatingSystem": "iOS", "applicationCategory": "FinanceApplication",
        "description": t["ld_desc"], "url": SITE + p["index"], "inLanguage": lang,
    }
    ld_faq = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]],
    }
    extra = (f'<script type="application/ld+json">{json.dumps(ld_app, ensure_ascii=False)}</script>\n'
             f'<script type="application/ld+json">{json.dumps(ld_faq, ensure_ascii=False)}</script>\n')
    h = head(lang, "index", t["title"], t["desc"], extra) + nav(lang, "index")

    b0 = t["bands"]
    h += f"""
  <main id="main">
  <section class="hero">
    <div>
      <div class="label">{t['hero_label']}</div>
      <h1>{t['hero_h1']}</h1>
      <p class="lead">{t['hero_lead']}</p>
      {cta(lang)}
      <p class="fine">{t['cta_fine']}</p>
    </div>
    <div class="phones">
      <div class="phone crop"><img src="/img/{lang}/flash.jpg" alt="{esc(b0[3]['alt'])}" width="1206" height="1640"></div>
      <div class="phone"><img src="/img/{lang}/networth.jpg" alt="{esc(b0[0]['alt'])}" width="1206" height="2622" loading="lazy"></div>
    </div>
  </section>
"""
    for i, b in enumerate(t["bands"]):
        flip = " flip" if i % 2 else ""
        anchor = ' id="features"' if i == 0 else ""
        pts = "".join(f"<li>{esc(x)}</li>" for x in b["pts"])
        crop = b["img"] == "flash"
        pcls = "phone crop" if crop else "phone"
        ph = 1640 if crop else 2622
        h += f"""
  <section class="band"{anchor}>
    <div class="row{flip}">
      <div class="copy">
        <div class="label">{b['label']}</div>
        <h2>{b['h2']}</h2>
        <p class="lead">{b['lead']}</p>
        <ul class="pts">{pts}</ul>
      </div>
      <div class="phones"><div class="{pcls}" style="width:min(70%,270px)"><img src="/img/{lang}/{b['img']}.jpg" alt="{esc(b['alt'])}" width="1206" height="{ph}" loading="lazy"></div></div>
    </div>
  </section>
"""
    cards = "".join(f'<div class="card"><h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for a, b in t["cards"])
    h += f"""
  <section class="band more">
    <div class="label">{t['more_label']}</div>
    <h2>{t['more_h2']}</h2>
    <p class="lead">{t['more_lead']}</p>
    <div class="cards">{cards}</div>
  </section>
  <section class="band about" id="about">
    <div class="in-narrow">
      <div class="label">{t['about_label']}</div>
      <h2>{t['about_h2']}</h2>
{''.join(f'      <p class="lead">{x}</p>' + chr(10) for x in t['about_p'])}      <a class="cta ghost" href="mailto:{EMAIL}?subject={t['about_subject'].replace(' ', '%20')}">{t['about_cta']}</a>
      <p class="fine">{EMAIL}</p>
    </div>
  </section>
  <section class="band faq" id="faq">
    <div class="label">{t['faq_label']}</div>
    <h2>{t['faq_h2']}</h2>
{''.join(f'      <details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' + chr(10) for q, a in t['faq'])}  </section>
  </main>
</div>

<div class="strip">
  <div class="in">
{''.join(f'    <div><b>{esc(a)}</b><span>{esc(b)}</span></div>' + chr(10) for a, b in t['strip'])}  </div>
</div>

<div class="in">
  <section class="close">
    <h2>{t['close_h2']}</h2>
    <p class="lead">{t['close_lead']}</p>
    {cta(lang, 'cta_close')}
    <p class="fine">{t['cta_fine']}</p>
  </section>
"""
    h += footer(lang)
    return h


def support(lang):
    t = T[lang]
    p = PATHS[lang]
    h = head(lang, "support", t["sup_title"], t["sup_desc"]) + nav(lang, "support")
    faq = "".join(f"  <details><summary>{esc(q)}</summary><p>{a.format(privacy=p['privacy'])}</p></details>\n" for q, a in t["sup_faq"])
    h += f"""  <main class="doc faq">
  <div class="label">{t['sup_eyebrow']}</div>
  <h1>{t['sup_h1']}</h1>
  <p class="sub">{t['sup_sub']}</p>
  <div class="contact"><p>{t['sup_contact']}</p></div>
  <h2>{t['sup_faq_h2']}</h2>
{faq}  <p class="fine" style="margin-top:36px"><a href="{p['privacy']}">{t['footer_privacy']}</a> · {t['sup_foot']}</p>
  </main>
"""
    h += footer(lang)
    return h


def privacy(lang):
    t = T[lang]
    pv = PRIVACY[lang]
    p = PATHS[lang]
    h = head(lang, "privacy", t["pri_title"], t["pri_desc"]) + nav(lang, "privacy")
    pills = "".join(f'<span class="pill">{esc(x)}</span>' for x in pv["pills"])
    th = "".join(f"<th>{esc(x)}</th>" for x in pv["stores_th"])
    rows = "".join(f'<tr><td class="type">{esc(a)}</td><td class="dim">{esc(b)}</td><td class="dim">{esc(c)}</td></tr>' for a, b, c in pv["stores"])

    def section(title, paras):
        return f"  <h2>{esc(title)}</h2>\n" + "".join(f"  <p>{x}</p>\n" for x in paras)

    ai_list = "  <ul>\n" + "".join(f"    <li>{x}</li>\n" for x in pv["ai_list"]) + "  </ul>\n"
    body = "".join(section(a, b) for a, b in pv["sections"]) + ai_list + f"  <p>{pv['after_ai']}</p>\n"
    body += "".join(section(a, b) for a, b in pv["sections2"])
    h += f"""  <main class="doc">
  <div class="label">{t['pri_eyebrow']}</div>
  <h1>{t['pri_h1']}</h1>
  <p class="sub">{t['pri_sub'].format(updated=UPDATED[lang])}</p>
  <div class="box">
    <p>{pv['box'][0]}</p>
    <p>{pv['box'][1]}</p>
    <div class="pills">{pills}</div>
  </div>
  <h2 class="first">{pv['stores_h2']}</h2>
  <table><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table>
{body}  <div class="contact">
    <h2>{pv['contact_h2']}</h2>
    <p>{pv['contact_p']} <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
  <p class="fine" style="margin-top:36px"><a href="{p['support']}">{t['footer_support']}</a> · {t['sup_foot']}</p>
  </main>
"""
    h += footer(lang)
    return h


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    for lang in ("en", "es"):
        write(FILES[lang]["index"], index(lang))
        write(FILES[lang]["support"], support(lang))
        write(FILES[lang]["privacy"], privacy(lang))
    urls = [SITE + PATHS[l][k] for l in ("en", "es") for k in ("index", "support", "privacy")]
    sm = ('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"<url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    write("CNAME", "freedompoint.app\n")
    print("built", len(urls), "pages")


if __name__ == "__main__":
    main()
