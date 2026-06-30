# -*- coding: utf-8 -*-
"""Body content for PrimeVolt inner pages. Imported by build_site.py."""

def build(g):
    page_hero=g['page_hero']; CTA=g['CTA']; head=g['head']; write=g['write']
    ARROW=g['ARROW']; CHECK=g['CHECK']; PIN=g['PIN']; MAIL=g['MAIL']; PHONE=g['PHONE']; GLOBE=g['GLOBE']
    C="https://www.primevoltes.ca/"

    def ic(path, cls=""):
        return '<div class="ic %s"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">%s</svg></div>' % (cls, path)

    def w3(subject):  # Web3Forms hidden fields (replace the access key to go live)
        return ('<input type="hidden" name="access_key" value="REPLACE_WITH_WEB3FORMS_ACCESS_KEY">'
                '<input type="hidden" name="subject" value="' + subject + '">'
                '<input type="hidden" name="from_name" value="PrimeVolt Website">'
                '<input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off">')

    # ============================================================= ABOUT
    body = page_hero("About",
        "An Ontario power-infrastructure firm built on deep transmission expertise",
        "PrimeVolt Energy Systems provides specialist support for high-voltage transmission, grid maintenance and modernization — led by a founder with 24 years in the sector.")
    body += ('<section class="section"><div class="container"><div class="feature">'
      '<div class="feature-copy reveal"><span class="eyebrow">Who we are</span>'
      '<h2>Specialist support for Ontario\'s electricity network</h2>'
      '<p class="lead">PrimeVolt Energy Systems is an Ontario-focused power-infrastructure business providing high-voltage transmission line support, grid maintenance coordination, upgrade planning and modernization assistance.</p>'
      '<p class="muted">Rather than launching as a capital-intensive construction contractor, PrimeVolt operates a lean, practical model — focusing first on technical support, project coordination, inspection support, documentation, maintenance planning and smart-grid integration assistance for utilities, contractors, industrial clients and energy-sector partners. This builds market presence gradually while keeping operating risk controlled.</p>'
      '<div style="margin-top:26px"><a class="btn btn-primary" href="services.html">Explore our services ' + ARROW + '</a></div></div>'
      '<div class="feature-media reveal d1"><div class="frame pad" style="min-height:360px;display:flex;flex-direction:column;justify-content:center;gap:16px">'
      '<div style="color:#fff;font-family:Sora;font-weight:700;font-size:1.1rem;margin-bottom:4px">At a glance</div>'
      + ''.join('<div style="display:flex;justify-content:space-between;gap:16px;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.1)"><span style="color:#a9c2da">%s</span><span style="color:#fff;font-family:Sora;font-weight:600;text-align:right">%s</span></div>' % (k,v) for k,v in [
        ("Legal entity","PrimeVolt Energy Systems Ltd."),("Jurisdiction","Ontario, Canada"),
        ("Ontario Corp. No.","1001613569"),("Incorporated","21 May 2026"),
        ("Focus","HV transmission &amp; grid"),("Founder experience","24+ years")])
      + '</div></div></div></div></section>')
    # mission / vision
    body += ('<section class="section section--navy"><div class="container"><div class="grid grid-2">'
      '<div class="card reveal" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12)">'
      + ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>') +
      '<h3 style="color:#fff">Mission</h3><p style="color:#b9cee2">To design, construct and modernize high-voltage transmission lines and power grids, ensuring reliable, efficient and sustainable electricity delivery — integrating smart-grid technologies, renewable solutions and advanced automation to support Canada\'s energy transition and grid resilience.</p></div>'
      '<div class="card reveal d1" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12)">'
      + ic('<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/>','gold') +
      '<h3 style="color:#fff">Vision</h3><p style="color:#b9cee2">To be a leading provider of advanced transmission and grid-modernization services in Canada — driving a smarter, greener and more reliable energy future, and empowering communities with secure, sustainable power.</p></div>'
      '</div></div></section>')
    # founder
    body += ('<section class="section"><div class="container"><div class="section-head reveal"><span class="eyebrow">The founder</span>'
      '<h2>Rana Muhammad Zahid Hafeez</h2><p class="lead">Founder &amp; Principal Consultant — 24 years in power transmission and grid infrastructure.</p></div>'
      '<div class="founder-card reveal"><div class="founder-photo"><div class="ph-mono">RZ</div><div class="ph-tag">Founder &amp; Principal Consultant</div></div>'
      '<div class="founder-body"><p class="muted">A highly accomplished engineering professional with 24 years of experience in power transmission and grid infrastructure, Rana has managed and executed high-profile, technically complex energy projects. His expertise spans high-voltage transmission, grid-station development and HVDC systems — including a pivotal role on the &plusmn;660&nbsp;kV Matiari&ndash;Lahore HVDC line, the first DC transmission project under the CPEC initiative.</p>'
      '<p class="muted">As Founder-Operator he leads PrimeVolt\'s strategy, business development, technical quality, project coordination and client relationships in Ontario &mdash; an active, hands-on operator rather than a passive investor.</p>'
      '<h3 style="font-size:1.05rem;margin-top:8px">Core competencies</h3><div class="chips">'
      + ''.join('<span class="chip">%s</span>' % c for c in ["High-Voltage Transmission 33&ndash;500 kV","Grid-Station Construction &amp; Augmentation","HVDC Project Management","Renewable Energy Integration","Tender &amp; BOQ Management","Testing &amp; Commissioning"])
      + '</div></div></div></div></section>')
    # experience timeline
    exp = [("Mar 2022 &ndash; Present","Additional Deputy Manager (Technical), NTDC","Spearheaded EHV transmission projects across 500/220/132 kV lines and grid stations; managed ~300 km of the 886 km HVDC line; led patrolling, maintenance and complex tender/BOQ documentation."),
           ("Feb 2014 &ndash; Mar 2022","Assistant Deputy Manager, NTDC","Managed 500 kV substation upgrades and delivery of major lines including the 220 kV Lahore North and 500 kV AIS Grid Station Sheikhupura; led construction, testing and commissioning."),
           ("Nov 2011 &ndash; Jan 2014","Electrical Engineer, M/S China Petroleum (CPECC)","Directed construction of 33 kV overhead and underground transmission lines in Sudan, from design to commissioning, including grounding systems and RMU installations.")]
    body += ('<section class="section section--mist"><div class="container"><div class="section-head reveal"><span class="eyebrow">Track record</span><h2>Leadership &amp; professional experience</h2></div>'
      '<div class="grid" style="gap:18px">'
      + ''.join('<div class="card reveal" style="display:grid;grid-template-columns:200px 1fr;gap:24px;align-items:start"><div><div style="font-family:Sora;font-weight:700;color:var(--blue-600)">%s</div></div><div><h3 style="font-size:1.12rem;margin-bottom:6px">%s</h3><p>%s</p></div></div>' % (d,t,desc) for d,t,desc in exp)
      + '</div></div></section>')
    # values
    vals = [("Reliability","Consistent, dependable delivery across a network of more than 30,000 circuit km that underpins economic activity and daily life."),
            ("Innovation","Advancing grid technologies in line with Canada\'s clean-electricity strategy and the sector\'s long-term growth."),
            ("Economic Growth","Supporting job creation and infrastructure delivery in a sector adding thousands of new roles as the grid transitions."),
            ("Sustainability","Helping integrate renewables and maintain a grid that is already more than 90% emissions-free."),
            ("Workforce Development","Building skilled, safety-focused capability ready for grid modernization and automation.")]
    vbody=''
    for i,(t,d) in enumerate(vals):
        vbody += ('<div class="value-card reveal %s"><div class="vh"><span class="dot">%s</span><h3>%s</h3></div><p>%s</p></div>'
                  % ('d1' if i%2 else '', CHECK, t, d))
    body += ('<section class="section"><div class="container"><div class="section-head center reveal"><span class="eyebrow">What guides us</span><h2>Our values</h2></div>'
      '<div class="grid grid-3">' + vbody + '</div></div></section>')
    body += CTA
    write('about.html','about.html', head('About PrimeVolt Energy Systems | Founder &amp; Company',
      'Learn about PrimeVolt Energy Systems, an Ontario power-infrastructure firm, and founder Rana Muhammad Zahid Hafeez — 24 years in high-voltage transmission, grid stations and HVDC.',
      C+'about.html'), body)

    # ============================================================= SERVICES
    services = [
      ("Transmission Line Support &amp; Upgrade Assistance","M3 21h18M6 21V8l6-5 6 5v13M9 21v-5h6v5",
       "Technical coordination, project support, maintenance planning, inspection assistance and documentation for transmission expansion and upgrade activities.",
       ["Project readiness &amp; coordination","Inspection &amp; field documentation","Upgrade planning support","Reliability improvement"]),
      ("Grid Maintenance Coordination","M14.7 6.3a5 5 0 0 0-7 7l1.5-1.5M9.3 17.7a5 5 0 0 0 7-7 M3 21l5-5M21 3l-5 5",
       "Preventive maintenance scheduling, field reporting, inspection support and technical follow-up that reduce operational disruptions and improve asset performance.",
       ["Preventive maintenance scheduling","Field reporting &amp; follow-up","Outage planning support","Asset performance tracking"]),
      ("Smart-Grid &amp; Modernization Support","M9 9h6v6H9z M2 10h2M2 14h2M20 10h2M20 14h2M10 2v2M14 2v2M10 20v2M14 20v2",
       "Support for digital reporting, monitoring coordination, maintenance optimization and smart-grid integration to improve operational visibility and grid resilience.",
       ["Monitoring coordination","Maintenance optimization","Modernization readiness","Operational visibility"]),
      ("Renewable Energy Integration Support","M12 3v18M5 8s2-3 7-3 7 3 7 3M3 14c2 2 5 3 9 3s7-1 9-3",
       "Technical coordination, planning assistance and infrastructure-readiness support for smoother integration of cleaner, more flexible power sources.",
       ["Connection-related coordination","Planning &amp; documentation","Infrastructure readiness","Grid-flexibility support"]),
      ("Technical Documentation, BOQ &amp; Tender","M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z M14 2v6h6M9 13h6M9 17h6",
       "Tender preparation, BOQ support, technical specifications, project records and coordination documents — high-value, low-capital, founder-led expertise.",
       ["Tender preparation","Bills of Quantities (BOQ)","Technical specifications","Project records"]),
      ("Project Coordination &amp; Contractor Liaison","M12 8a3 3 0 1 0 0 0 M5 6a2 2 0 1 0 0 0 M19 6a2 2 0 1 0 0 0 M7 6h2M15 6h2",
       "Contractor liaison, schedule management and stakeholder coordination that keep transmission and grid projects moving smoothly and on time.",
       ["Contractor liaison","Schedule management","Stakeholder coordination","Service follow-up"]),
    ]
    body = page_hero("Services","Specialist services across the transmission value chain",
       "From documentation and maintenance coordination to smart-grid modernization — a flexible, founder-led model designed for utilities, contractors and industrial clients in Ontario.")
    cards=''
    for i,(t,p,desc,feats) in enumerate(services):
        feat_html=''.join('<li>%s<span>%s</span></li>' % (CHECK,f) for f in feats)
        cards += ('<article class="card reveal %s"><div class="num">%02d</div>%s<h3>%s</h3><p>%s</p>'
          '<ul class="ticks" style="margin-top:16px">%s</ul></article>'
          % ('d1' if i%3==1 else ('d2' if i%3==2 else ''), i+1,
             ic(p, ['','gold','navy'][i%3]), t, desc, feat_html))
    body += '<section class="section"><div class="container"><div class="grid grid-2">' + cards + '</div></div></section>'
    # scalable model
    body += ('<section class="section section--navy"><div class="container"><div class="feature">'
      '<div class="feature-copy reveal"><span class="eyebrow">How we work</span><h2 style="color:#fff">A scalable, low-capital service model</h2>'
      '<p class="lead" style="color:#b9cee2">PrimeVolt begins with lower-capital technical and coordination services and expands gradually through subcontracting partnerships and client relationships &mdash; entering Ontario\'s infrastructure market responsibly while building credibility.</p>'
      '<ul class="ticks"><li>' + CHECK + '<span style="color:#cfe0f0"><b style="color:#fff">Phase 1</b> &mdash; technical consulting, documentation, BOQ &amp; tender support, maintenance coordination.</span></li>'
      '<li>' + CHECK + '<span style="color:#cfe0f0"><b style="color:#fff">Phase 2</b> &mdash; broader field-support and project-execution via specialist partnerships.</span></li>'
      '<li>' + CHECK + '<span style="color:#cfe0f0"><b style="color:#fff">Phase 3</b> &mdash; recurring support arrangements and higher-value modernization assistance.</span></li></ul></div>'
      '<div class="feature-media reveal d1"><div class="frame pad" style="min-height:320px;display:flex;flex-direction:column;justify-content:center;gap:14px">'
      + ''.join('<div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:16px 18px"><div style="width:38px;height:38px;border-radius:10px;background:%s;display:grid;place-items:center;color:#fff;font-family:Sora;font-weight:700;flex:none">%s</div><div style="color:#fff;font-family:Sora;font-weight:600">%s</div></div>' % (bg,n,lab)
        for n,lab,bg in [("1","Engage &amp; scope","linear-gradient(135deg,#34D17E,#1FA85C)"),("2","Coordinate &amp; document","linear-gradient(135deg,#FFD774,#F59E0B)"),("3","Deliver &amp; follow up","linear-gradient(135deg,#34D399,#10B981)"),("4","Sustain &amp; grow","linear-gradient(135deg,#A7E9C6,#178A49)")])
      + '</div></div></div></div></section>')
    body += CTA
    write('services.html','services.html', head('Services | PrimeVolt Energy Systems',
      'Transmission line support, grid maintenance coordination, smart-grid modernization, renewable integration, BOQ &amp; tender support and project coordination across Ontario.',
      C+'services.html','grid modernization Ontario, smart grid integration, high-voltage transmission support, BOQ tender support'), body)

    # ============================================================= INDUSTRY
    body = page_hero("Industry","The Ontario opportunity: a structural, multi-decade reinvestment cycle",
       "Rising demand, ageing assets and modernization are converging. Ontario\'s electricity demand is forecast to grow 75% by 2050 — driving sustained need for transmission support services.")
    # key indicators
    inds=[("151 &rarr; 263 TWh","Ontario electricity demand, 2025&ndash;2050"),("+75%","Demand growth by 2050"),
          ("30,000 km","Hydro One high-voltage network"),("97%","Ontario transmission owned by Hydro One")]
    body += ('<section class="section"><div class="container"><div class="stats">'
      + ''.join('<div class="stat reveal %s"><div class="n" style="font-size:1.7rem">%s</div><div class="l">%s</div></div>' % ('d%d'%(i) if i else '', n, l) for i,(n,l) in enumerate(inds))
      + '</div></div></section>')
    # supply mix bars
    mix=[("Nuclear",48.5,"#178A49"),("Waterpower",23.4,"#1FA85C"),("Gas / Oil / Other",16.6,"#5B7185"),("Wind",9.0,"#34D399"),("Solar",2.2,"#F59E0B"),("Bioenergy",0.4,"#A7E9C6")]
    bars=''
    for name,pct,col in mix:
        bars += ('<div style="margin-bottom:16px"><div style="display:flex;justify-content:space-between;margin-bottom:6px">'
          '<span style="font-weight:600;color:var(--navy)">%s</span><span style="font-family:Sora;font-weight:700;color:var(--navy)">%s%%</span></div>'
          '<div style="height:12px;background:var(--mist-2);border-radius:8px;overflow:hidden"><div style="height:100%%;width:%s%%;background:%s;border-radius:8px"></div></div></div>'
          % (name,pct,pct,col))
    body += ('<section class="section section--mist"><div class="container"><div class="feature">'
      '<div class="feature-copy reveal"><span class="eyebrow">2024 supply mix</span><h2>A diversified, largely low-carbon grid</h2>'
      '<p class="lead">Ontario\'s electricity system is more than 90% emissions-free &mdash; led by nuclear and waterpower. This diversified mix supports reliability but demands continuous grid balancing, transmission coordination and modernization planning.</p>'
      '<p class="muted">For PrimeVolt, the implication is clear: Ontario does not just need new lines &mdash; it needs practical support services that help maintain and modernize a complex operating network.</p></div>'
      '<div class="feature-media reveal d1"><div class="card" style="padding:34px">' + bars + '</div></div></div></div></section>')
    # pipeline
    proj=[("Windsor &ndash; Lakeshore","Southwestern Ontario","230 kV line","Supports industrial load growth and regional reinforcement."),
          ("Waasigan Transmission Line","Northwestern Ontario","~190 km, 230 kV","Major line construction and coordination outside the GTA."),
          ("Sudbury &ndash; Barrie","Northern to Central","~300 km, 500 kV (proposed)","Long-horizon growth in backbone transmission."),
          ("Third downtown Toronto line","Toronto","Planning / advancement","Infrastructure pressure in high-density urban demand.")]
    body += ('<section class="section"><div class="container"><div class="section-head reveal"><span class="eyebrow">Project pipeline</span>'
      '<h2>Demand is already converting into real infrastructure</h2><p class="lead">In 2025 the Ontario government announced new transmission lines and major upgrades. Selected developments shaping market demand:</p></div>'
      '<div class="grid grid-2">'
      + ''.join('<div class="card reveal %s"><div style="display:flex;justify-content:space-between;align-items:start;gap:14px"><h3 style="font-size:1.12rem">%s</h3><span class="badge-soft">%s</span></div><div class="muted" style="font-size:.9rem;margin:6px 0 10px">%s</div><p>%s</p></div>' % ('d1' if i%2 else '',t,scale,region,why) for i,(t,region,scale,why) in enumerate(proj))
      + '</div></div></section>')
    # drivers / fit
    body += ('<section class="section section--navy"><div class="container"><div class="grid grid-3">'
      + ''.join('<div class="card reveal %s" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12)">%s<h3 style="color:#fff">%s</h3><p style="color:#b9cee2">%s</p></div>'
        % (['','d1','d2'][i], ic(p,['','gold','navy'][i]), t, d)
        for i,(t,p,d) in enumerate([
          ("Electrification-led demand","<path d='M13 2 3 14h7l-1 8 10-12h-7l1-8z'/>","EV supply chains, industrial growth, data centres and housing are driving higher electricity use and stronger transmission needs."),
          ("Ageing assets","<path d='M12 8v4l3 2'/><circle cx='12' cy='12' r='9'/>","Hydro One\'s investment narrative emphasizes renewing and replacing ageing infrastructure &mdash; recurring maintenance and technical-support work."),
          ("System modernization","<rect x='4' y='4' width='16' height='16' rx='2'/><path d='M9 9h6v6H9z'/>","Ontario is improving how the system is monitored and operated &mdash; favouring firms that bridge field operations, reporting and modernization."),
        ]))
      + '</div></div></section>')
    body += CTA
    write('industry.html','industry.html', head('Industry &amp; Market | Ontario Transmission &amp; Grid Modernization',
      'Ontario electricity demand is forecast to rise 75% by 2050. Explore the market drivers, supply mix, transmission project pipeline and where PrimeVolt fits.',
      C+'industry.html','Ontario transmission market, grid modernization Ontario, electricity demand 2050, Hydro One capital plan'), body)

    # ============================================================= CAREERS
    body = page_hero("Careers","Building skilled energy careers &mdash; and contributing to Ontario\'s economy",
       "As Ontario\'s power infrastructure modernizes and grows, PrimeVolt is committed to creating meaningful job opportunities and supporting workforce development across the province.")
    body += ('<section class="section"><div class="container"><div class="section-head reveal"><span class="eyebrow">Economic contribution</span>'
      '<h2>Creating Canadian jobs as the grid expands</h2><p class="lead">Ontario\'s utilities sector employed 59,500 people and contributed $16.1&nbsp;billion to GDP in 2024, with demand for skilled labour expected to stay strong. PrimeVolt will add specialized roles, knowledge transfer and contract opportunities as it grows.</p></div>'
      '<div class="grid grid-3">'
      + ''.join('<div class="card reveal %s">%s<h3>%s</h3><p>%s</p></div>' % (['','d1','d2'][i%3], ic(p,['','gold','navy'][i%3]), t, d)
        for i,(t,p,d) in enumerate([
          ("Skilled Electricians &amp; Line Technicians","<path d='M3 21h18M6 21V8l6-5 6 5v13'/>","To construct, maintain and upgrade high-voltage transmission lines and support reliable power across Ontario\'s regions."),
          ("Power Systems Engineers &amp; Designers","<circle cx='12' cy='12' r='3'/><path d='M12 2v3M12 19v3M2 12h3M19 12h3'/>","Specializing in power systems, electrical infrastructure and renewable integration to design grid-modernization strategies."),
          ("IT &amp; Smart-Grid Technologists","<rect x='3' y='4' width='18' height='12' rx='2'/><path d='M8 20h8'/>","In cybersecurity, data analysis and IoT connectivity to integrate advanced grid-management systems and improve efficiency."),
          ("Project Managers &amp; Safety Supervisors","<path d='M9 11l3 3 8-8'/><path d='M20 12v6a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h9'/>","To oversee grid projects, ensure timely delivery, manage budgets and enforce strict safety compliance."),
          ("Training &amp; Apprenticeships","<path d='M22 10 12 5 2 10l10 5 10-5z'/><path d='M6 12v5c0 1 3 3 6 3s6-2 6-3v-5'/>","Partnering with technical colleges and universities to provide on-the-job training and certifications for emerging talent."),
          ("Subcontract &amp; Specialist Partners","<circle cx='9' cy='12' r='3'/><circle cx='17' cy='12' r='3'/>","Contract professionals and partner specialists who participate in Ontario electricity-infrastructure projects."),
        ]))
      + '</div></div></section>')
    # why join
    body += ('<section class="section section--mist"><div class="container"><div class="feature reverse">'
      '<div class="feature-media reveal"><div class="frame pad" style="min-height:320px;display:flex;flex-direction:column;justify-content:center;gap:14px">'
      + ''.join('<div style="display:flex;gap:13px;align-items:flex-start;color:#cfe0f0"><span style="color:#FFD774;flex:none">%s</span><span><b style="color:#fff;font-family:Sora">%s</b><br><span style="color:#a9c2da;font-size:.92rem">%s</span></span></div>' % (CHECK,t,d)
        for t,d in [("Mentorship from a senior expert","Learn directly from 24 years of transmission and grid experience."),("Meaningful, modern work","Contribute to Ontario\'s clean-energy transition and grid modernization."),("Growth pathways","Skills transfer, certifications and a culture of continuous improvement."),("Safety-first culture","High professional and safety standards on every engagement.")])
      + '</div></div>'
      '<div class="feature-copy reveal d1"><span class="eyebrow">Why join PrimeVolt</span><h2>Grow with Ontario\'s energy future</h2>'
      '<p class="lead">PrimeVolt is building a workforce-development platform &mdash; promoting inclusivity, diversity and career pathways in an industry that needs skilled people.</p>'
      '<p class="muted">We are an early-stage, founder-led business. If you are a technician, engineer, coordinator or specialist who wants to be part of building something with Ontario\'s grid at its core, we\'d like to hear from you.</p></div></div></div></section>')
    # express interest form
    body += ('<section class="section"><div class="container"><div class="feature">'
      '<div class="feature-copy reveal"><span class="eyebrow">Express interest</span><h2>Register your interest</h2>'
      '<p class="lead">We\'re building a talent pipeline for upcoming roles. Share your details and area of expertise, and we\'ll be in touch as opportunities open.</p>'
      '<ul class="ticks"><li>' + MAIL + '<span>Or email <a href="mailto:careers@primevoltes.ca">careers@primevoltes.ca</a></span></li>'
      '<li>' + PHONE + '<span><a href="tel:+14375592990">+1 (437) 559-2990</a></span></li></ul></div>'
      '<div class="feature-media reveal d1"><div class="form-card"><form data-form>'
      '<div class="row-2"><div class="field"><label>Full name</label><input type="text" name="name" required></div>'
      '<div class="field"><label>Email</label><input type="email" name="email" required></div></div>'
      '<div class="field"><label>Area of expertise</label><select name="area"><option>Line Technician / Electrician</option><option>Power Systems Engineer</option><option>IT / Smart-Grid</option><option>Project Management / Safety</option><option>Apprenticeship / Trainee</option><option>Other</option></select></div>'
      '<div class="field"><label>Tell us about your experience</label><textarea name="message"></textarea></div>'
      '<div class="field hp"><label>Leave blank</label><input type="text" name="company_website" tabindex="-1" autocomplete="off"></div>'
      + w3('New careers interest &mdash; PrimeVolt') +
      '<button class="btn btn-primary" type="submit" style="width:100%;justify-content:center">Submit interest</button>'
      '<p class="form-result" style="display:none;color:#10B981;font-weight:600;margin-top:14px"></p>'
      '<p class="form-note">By submitting you agree to be contacted about opportunities at PrimeVolt Energy Systems.</p>'
      '</form></div></div></div></div></section>')
    write('careers.html','careers.html', head('Careers &amp; Job Creation | PrimeVolt Energy Systems',
      'PrimeVolt Energy Systems is creating skilled energy-sector jobs in Ontario — electricians, engineers, smart-grid technologists, project managers and apprenticeships. Register your interest.',
      C+'careers.html','energy jobs Ontario, electrician jobs, power systems engineer, grid careers'), body)

    # ============================================================= INSIGHTS
    from build_articles import ARTICLES
    body = page_hero("Insights","Insights on Ontario\'s energy transition",
       "Perspectives, guides and analysis on grid modernization, smart-grid integration and renewable energy transmission — written to inform utilities, contractors and industrial clients.")
    # featured
    f=ARTICLES[0]
    body += ('<section class="section"><div class="container"><a class="post reveal" href="' + f['slug'] + '.html" style="display:grid;grid-template-columns:1.1fr 1fr;align-items:stretch">'
      '<div class="post-img" style="background:' + f['bg'] + ';height:auto;min-height:300px"><span class="tag">Featured &middot; ' + f['tag'] + '</span></div>'
      '<div class="post-body" style="padding:40px"><div class="date">' + f['kind'] + ' &middot; ' + f['read'] + '</div><h3 style="font-size:1.6rem">' + f['title'] + '</h3><p style="font-size:1rem">' + f['excerpt'] + '</p>'
      '<span class="card-link" style="margin-top:18px">Read article ' + ARROW + '</span></div></a></div></section>')
    # grid of rest
    cards=''
    for i,a in enumerate(ARTICLES[1:]):
        cards += ('<a class="post reveal ' + ['','d1','d2'][i%3] + '" href="' + a['slug'] + '.html"><div class="post-img" style="background:' + a['bg'] + '"><span class="tag">' + a['tag'] + '</span></div>'
          '<div class="post-body"><div class="date">' + a['kind'] + '</div><h3>' + a['title'] + '</h3><p>' + a['excerpt'] + '</p>'
          '<span class="card-link">Read more ' + ARROW + '</span></div></a>')
    body += '<section class="section section--mist"><div class="container"><div class="section-head reveal"><span class="eyebrow">Latest articles</span><h2>More from PrimeVolt</h2></div><div class="grid grid-3">' + cards + '</div></div></section>'
    # newsletter
    body += ('<section class="section"><div class="container"><div class="cta-band reveal"><div class="ctaglow"></div><div style="position:relative;z-index:2;max-width:640px">'
      '<span class="eyebrow" style="color:var(--gold-soft)">Stay informed</span><h2>Ontario energy insights, in your inbox</h2>'
      '<p>Occasional briefings on grid modernization, transmission and the Ontario electricity market. No spam.</p>'
      '<form data-form style="display:flex;gap:12px;flex-wrap:wrap;margin-top:22px">'
      + w3('Newsletter signup &mdash; PrimeVolt') +
      '<input type="email" name="email" required placeholder="you@company.com" style="flex:1;min-width:240px;padding:14px 18px;border-radius:999px;border:1.5px solid rgba(255,255,255,.25);background:rgba(255,255,255,.1);color:#fff">'
      '<button class="btn btn-gold" type="submit">Subscribe</button>'
      '<p class="form-result" style="display:none;color:#FFD774;font-weight:600;width:100%"></p></form></div></div></div></section>')
    write('insights.html','insights.html', head('Insights | PrimeVolt Energy Systems',
      'Articles and analysis on grid modernization, smart-grid integration and renewable energy transmission in Ontario.',
      C+'insights.html','grid modernization, smart grid integration, renewable energy transmission, Ontario energy'), body)

    # ============================================================= CONTACT
    body = page_hero("Contact","Let\'s talk about your transmission or grid project",
       "Tell us what you need — technical support, maintenance coordination, documentation or modernization assistance — and we\'ll respond promptly.")
    tiles=[("Telephone",PHONE,"+1 (437) 559-2990","tel:+14375592990"),
           ("Email",MAIL,"info@primevoltes.ca","mailto:info@primevoltes.ca"),
           ("Website",GLOBE,"www.primevoltes.ca","https://www.primevoltes.ca"),
           ("Location",PIN,"Greater Toronto Area, Ontario, Canada",None)]
    tiles_html=''
    for k,icon,val,href in tiles:
        inner = ('<a href="%s" class="val">%s</a>' % (href,val)) if href else ('<div class="val">%s</div>' % val)
        tiles_html += '<div class="contact-tile reveal"><div class="ci">%s</div><div><div class="k">%s</div>%s</div></div>' % (icon,k,inner)
    body += ('<section class="section"><div class="container"><div class="feature">'
      '<div class="feature-media reveal"><div class="form-card"><h3 style="margin-bottom:6px">Request a consultation</h3>'
      '<p class="muted" style="font-size:.95rem;margin-bottom:22px">Fields marked * are required.</p><form data-form>'
      '<div class="row-2"><div class="field"><label>Full name *</label><input type="text" name="name" required></div>'
      '<div class="field"><label>Company</label><input type="text" name="company"></div></div>'
      '<div class="row-2"><div class="field"><label>Email *</label><input type="email" name="email" required></div>'
      '<div class="field"><label>Phone</label><input type="tel" name="phone"></div></div>'
      '<div class="field"><label>Service of interest</label><select name="service">'
      '<option>Transmission Line Support</option><option>Grid Maintenance Coordination</option><option>Smart-Grid &amp; Modernization</option><option>Renewable Integration Support</option><option>Documentation, BOQ &amp; Tender</option><option>Project Coordination</option><option>General enquiry</option></select></div>'
      '<div class="field"><label>Message *</label><textarea name="message" required></textarea></div>'
      '<div class="field hp"><label>Leave blank</label><input type="text" name="company_website" tabindex="-1" autocomplete="off"></div>'
      + w3('New website enquiry &mdash; PrimeVolt') +
      '<button class="btn btn-primary" type="submit" style="width:100%;justify-content:center">Send message ' + ARROW + '</button>'
      '<p class="form-result" style="display:none;color:#10B981;font-weight:600;margin-top:14px"></p>'
      '<p class="form-note">We aim to respond within one business day. Prefer email? Write to <a href="mailto:info@primevoltes.ca">info@primevoltes.ca</a>.</p>'
      '</form></div></div>'
      '<div class="feature-copy reveal d1"><span class="eyebrow">Get in touch</span><h2>Contact PrimeVolt Energy Systems</h2>'
      '<p class="lead">Founder-led and responsive. Reach out directly and speak with someone who understands transmission and grid work.</p>'
      '<div class="grid" style="gap:14px;margin-top:8px">' + tiles_html + '</div>'
      '<div style="margin-top:20px;padding:16px 20px;background:var(--mist);border:1px solid var(--line);border-radius:14px;font-size:.9rem;color:var(--slate)">'
      '<b style="color:var(--navy)">Business hours</b><br>Monday&ndash;Friday, 9:00&ndash;18:00 ET</div>'
      '</div></div></div></section>')
    # map placeholder
    body += ('<section class="section--tight" style="padding-bottom:90px"><div class="container">'
      '<div class="reveal" style="border-radius:var(--radius-lg);overflow:hidden;border:1px solid var(--line);height:300px;background:'
      'linear-gradient(135deg,#0F3157,#0A2240);display:grid;place-items:center;position:relative">'
      '<svg viewBox="0 0 1200 300" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0;width:100%;height:100%;opacity:.25" xmlns="http://www.w3.org/2000/svg">'
      '<g stroke="#34D17E" stroke-width="1" fill="none"><path d="M0 150 Q300 100 600 160 T1200 130"/><path d="M0 220 Q300 180 600 230 T1200 200"/></g></svg>'
      '<div style="text-align:center;color:#fff;position:relative;z-index:2"><div style="color:#FFD774;display:inline-flex;margin-bottom:8px">' + PIN + '</div>'
      '<div style="font-family:Sora;font-weight:700;font-size:1.2rem">Greater Toronto Area, Ontario</div>'
      '<div style="color:#a9c2da;font-size:.9rem;margin-top:4px">Serving utilities, contractors &amp; industrial clients across Ontario</div></div></div></div></section>')
    write('contact.html','contact.html', head('Contact | PrimeVolt Energy Systems',
      'Contact PrimeVolt Energy Systems — call +1 (437) 559-2990 or email info@primevoltes.ca. Request a consultation for transmission support, grid maintenance or modernization in Ontario.',
      C+'contact.html'), body)

    # ============================================================= 404
    body = ('<section class="page-hero" style="padding:200px 0 160px;text-align:center"><div class="hero-glow"></div>'
      '<div class="container"><div style="font-family:Sora;font-weight:800;font-size:6rem;line-height:1;color:#fff">404</div>'
      '<h1 style="margin-top:10px">This page could not be found</h1>'
      '<p style="margin:0 auto 28px">The page you\'re looking for may have moved. Let\'s get you back on track.</p>'
      '<div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap"><a class="btn btn-primary" href="index.html">Back to home ' + ARROW + '</a>'
      '<a class="btn btn-light" href="contact.html">Contact us</a></div></div></section>')
    write('404.html','', head('Page not found | PrimeVolt Energy Systems',
      'The page you are looking for could not be found.', C+'404.html'), body)

    # ============================================================= PRIVACY
    secs = [
      ("Overview","This Privacy Policy explains how PrimeVolt Energy Systems Limited (\"PrimeVolt\", \"we\", \"us\") collects, uses and protects information when you visit www.primevoltes.ca or contact us. This is a general template and should be reviewed by a qualified professional before publication."),
      ("Information we collect","When you submit an enquiry or careers form, we collect the details you provide — such as your name, company, email, phone number and message. We may also collect anonymous usage data (e.g., pages visited) through analytics tools to improve the site."),
      ("How we use information","We use your information to respond to enquiries, discuss potential services or roles, and improve our website. We do not sell your personal information."),
      ("Cookies &amp; analytics","Our site may use cookies and privacy-respecting analytics (such as Google Analytics) to understand how visitors use the site. You can control cookies through your browser settings."),
      ("Sharing","We may share information with service providers that help us operate the website or communicate with you (for example, email or form-handling services), under appropriate confidentiality obligations."),
      ("Data retention","We retain enquiry information only as long as necessary to respond to you and for legitimate business or legal purposes."),
      ("Your rights","You may request access to, correction of, or deletion of your personal information by contacting us at info@primevoltes.ca."),
      ("Contact","Questions about this policy? Email <a href=\"mailto:info@primevoltes.ca\">info@primevoltes.ca</a> or call <a href=\"tel:+14375592990\">+1 (437) 559-2990</a>."),
    ]
    body = page_hero("Privacy", "Privacy Policy", "How PrimeVolt Energy Systems handles your information.")
    inner = ''.join('<h2>%s</h2><p>%s</p>' % (t, d) for t, d in secs)
    body += ('<section class="section"><div class="container"><div class="prose reveal" style="margin:0 auto">'
      '<p class="muted">Last updated: ' + 'May 2026' + '</p>' + inner + '</div></div></section>')
    write('privacy.html','', head('Privacy Policy | PrimeVolt Energy Systems',
      'Privacy Policy for PrimeVolt Energy Systems — how we collect, use and protect your information.', C+'privacy.html'), body)
