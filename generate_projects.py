import os

NAV = '''<nav class="topnav">
  <div class="nav-links">
    <a href="index.html">Home</a>
    <a href="resume.html">Resume</a>
    <a href="projects.html">Projects</a>
  </div>
  <div class="nav-title">Ranvir Chennupalli's Portfolio</div>
  <div class="nav-social">
    <a href="#" title="LinkedIn (add your URL)" aria-label="LinkedIn">
      <svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.5 8h4V23h-4V8zm7.5 0h3.8v2.05h.05c.53-1 1.83-2.05 3.77-2.05C19.9 8 21 10.13 21 13.5V23h-4v-8.3c0-2-.04-4.5-2.75-4.5-2.75 0-3.17 2.15-3.17 4.36V23h-4V8z"/></svg>
    </a>
    <a href="#" title="GitHub (add your URL)" aria-label="GitHub">
      <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .3a12 12 0 00-3.8 23.4c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.6-4-1.6-.5-1.4-1.3-1.8-1.3-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-6a4.6 4.6 0 011.2-3.2 4.3 4.3 0 01.1-3.2s1-.3 3.3 1.2a11.5 11.5 0 016 0c2.3-1.5 3.3-1.2 3.3-1.2a4.3 4.3 0 01.1 3.2 4.6 4.6 0 011.2 3.2c0 4.7-2.8 5.7-5.5 6 .5.4.9 1.1.9 2.3v3.3c0 .3.2.7.8.6A12 12 0 0012 .3z"/></svg>
    </a>
    <a href="mailto:rpchennu@ncsu.edu" title="Email" aria-label="Email">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 6l10 7 10-7"/></svg>
    </a>
  </div>
</nav>'''

FOOTER = '''<footer>
  <div class="contact">
    <a href="mailto:rpchennu@ncsu.edu">rpchennu@ncsu.edu</a> · 919-889-0595 · Apex, NC
  </div>
  <div class="meta">Last updated 2026</div>
</footer>'''

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Ranvir Chennupalli</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

{nav}

<div class="detail-header wrap">
  <div class="detail-eyebrow">{eyebrow}</div>
  <h1 class="detail-title">{title}<span class="status-pill {status_class}">{status}</span></h1>
  <div class="detail-meta">{meta}</div>
</div>

<div class="gallery">
  <div class="g-main img-placeholder">
    Add a hero photo here<br>(save as <code>images/{slug}-1.jpg</code>)
  </div>
  <div class="img-placeholder">
    Add a photo here<br>(<code>images/{slug}-2.jpg</code>)
  </div>
  <div class="img-placeholder">
    Add a photo here<br>(<code>images/{slug}-3.jpg</code>)
  </div>
</div>

<div class="tag-row">
{tags}
</div>

<div class="detail-body">
  {body}
</div>

<div class="project-nav wrap">
  <a href="{prev_link}">← {prev_title}</a>
  <a href="projects.html">All Projects</a>
  <a href="{next_link}">{next_title} →</a>
</div>

{footer}

</body>
</html>
'''

PROJECTS = [
    {
        "slug": "windprofiler",
        "file": "project-windprofiler.html",
        "title": "Wind Profiler",
        "eyebrow": "Sailor Rover Dynamics · NC State",
        "status": "Active",
        "status_class": "active",
        "meta": "May 2026 — Present · Advisor: Andre Mazzoleni, Professor",
        "tags": ["Data Acquisition", "PCB Design (Altium)", "Python", "Instrumentation"],
        "body": """
        <p>The wind profiler is one of two custom data acquisition systems I designed and built
        for the Sailor Rover Dynamics lab. It autonomously scans a wind chamber and collects
        over 5,000 individually averaged data points per run — and in testing, it's proven more
        accurate than a hot-wire anemometer, the traditional instrument for this kind of
        measurement.</p>
        <h2>What I built</h2>
        <ul>
          <li>A dedicated custom PCB to drive the sensing and data collection hardware</li>
          <li>Firmware and control logic to autonomously sweep the wind chamber and log readings</li>
          <li>A Python pipeline that automatically organizes and names every output file by date
          and time, so months of runs stay usable without manual sorting</li>
        </ul>
        <h2>Why it matters</h2>
        <p>Together with a second DAQ system I built for rover position tracking, this system
        saved the lab over $2,500 in equipment costs that would otherwise have gone toward
        commercial instrumentation — while outperforming the standard tool for the job.</p>
        """,
    },
    {
        "slug": "windchamber",
        "file": "project-windchamber.html",
        "title": "Wind Chamber",
        "eyebrow": "Sailor Rover Dynamics · NC State",
        "status": "Active",
        "status_class": "active",
        "meta": "May 2026 — Present · Advisor: Andre Mazzoleni, Professor",
        "tags": ["Experimental Aerodynamics", "Test Apparatus", "Wind Tunnel Testing"],
        "body": """
        <p>The Sailor Rover achieves locomotion through aerodynamic lift and drag — a new
        paradigm in planetary rover movement — which means validating its aerodynamics in a
        controlled environment is central to the whole project. I assisted in developing and
        testing the lab's wind chamber, the facility used to evaluate rover configurations under
        controlled airflow.</p>
        <h2>What I worked on</h2>
        <ul>
          <li>Assisted in development and testing of the wind chamber/wind tunnel itself</li>
          <li>Designed and fabricated test apparatus for rolling resistance and wind tunnel
          evaluation of different rover configurations</li>
          <li>Used the chamber as the testbed for the wind profiler system, cross-validating its
          readings against known references</li>
        </ul>
        <h2>Why it matters</h2>
        <p>Every aerodynamic claim about the rover's performance — lift-to-drag ratios, loading
        predictions from CFD — ultimately gets checked against data from this chamber. Reliable
        physical test infrastructure is what makes the rest of the research trustworthy.</p>
        """,
    },
    {
        "slug": "rover-controls",
        "file": "project-rover-controls.html",
        "title": "Control Systems on Rover",
        "eyebrow": "Sailor Rover Dynamics · NC State",
        "status": "Active",
        "status_class": "active",
        "meta": "May 2026 — Present · Advisor: Andre Mazzoleni, Professor",
        "tags": ["PID Control", "PCB Design (Altium)", "Embedded Systems", "Data Acquisition"],
        "body": """
        <p>I'm leading development of the Sailor Rover's control system — an ongoing effort that
        starts with a PID control baseline and is building toward a fully custom, PCB-driven
        system integrating numerous motors, sensors, and electrical components.</p>
        <h2>Where it stands</h2>
        <ul>
          <li>Implementing PID control as the initial baseline for the rover's actuation</li>
          <li>Designing the path toward a custom PCB-driven control architecture that will
          replace the current setup as the system matures</li>
          <li>Built a rover position-tracking data acquisition system to derive acceleration from
          recorded motion data, feeding directly into control validation</li>
        </ul>
        <h2>Why it matters</h2>
        <p>The Sailor Rover's whole premise — locomotion through aerodynamic lift and drag — only
        works if the control system can actually coordinate the rover's motors and sensors in
        real time. This is the system that turns the aerodynamic concept into a rover that can
        actually move the way it's supposed to.</p>
        """,
    },
    {
        "slug": "archimedes-propeller",
        "file": "project-archimedes-propeller.html",
        "title": "Archimedes Propeller",
        "eyebrow": "Propeller Aeroacoustics Research · NC State",
        "status": "Complete",
        "status_class": "complete",
        "meta": "Aug 2025 — May 2026 · Advisor: Dr. Mingtai Chen",
        "tags": ["CFD", "ANSYS Fluent", "DDES / SST k–ω", "FW–H Aeroacoustics", "LabVIEW"],
        "body": """
        <p>This research focused on the aeroacoustics of propeller configurations — how propeller
        design choices translate into the noise a system generates, not just its aerodynamic
        performance. I ran high-fidelity CFD simulations and validated them against physical
        test data.</p>
        <h2>What I did</h2>
        <ul>
          <li>Ran DDES CFD simulations in ANSYS Fluent across 5 propeller configurations, using
          SST k–ω turbulence modeling and FW–H aeroacoustic modeling</li>
          <li>Built meshes up to 15.7 million cells with y+ &lt; 1, and evaluated thrust, torque,
          figure of merit, and acoustic directivity for each configuration</li>
          <li>Operated a physical thrust and acoustic test rig using LabVIEW, comparing
          experimental data directly against the CFD predictions</li>
          <li>Contributed to an AIAA 2026 abstract and partial manuscript before the research
          concluded in May 2026</li>
        </ul>
        <h2>Why it matters</h2>
        <p>Propeller noise is a real design constraint for many aircraft and drone applications,
        not just an afterthought. Being able to predict acoustic behavior computationally, and
        trust that prediction because it's validated against real test data, is what makes this
        kind of analysis useful for actual design decisions.</p>
        """,
    },
    {
        "slug": "clearwater-uav",
        "file": "project-clearwater-uav.html",
        "title": "ClearWater UAV",
        "eyebrow": "National TSA Competition",
        "status": "Complete",
        "status_class": "complete",
        "meta": "July 2024",
        "tags": ["Fluid Dynamics", "Propulsion Analysis", "UAV Design"],
        "body": """
        <p>ClearWater UAV was a two-stage unmanned vehicle designed for deep-ocean microplastic
        retrieval, built for the National TSA Competition. The system was validated to reach a
        400-meter target depth in testing.</p>
        <h2>What I worked on</h2>
        <ul>
          <li>Designed the two-stage vehicle architecture for deep-ocean deployment and retrieval</li>
          <li>Conducted fluid dynamics and propulsion analysis to optimize hull geometry and
          thruster selection for both stages of the vehicle</li>
          <li>Validated the system's ability to reach a 400m target depth through testing</li>
        </ul>
        <h2>Why it matters</h2>
        <p>Microplastic pollution is concentrated at depths that are difficult and expensive to
        reach with traditional oceanographic equipment. A two-stage vehicle approach — balancing
        depth capability against retrieval payload — was the core engineering trade-off this
        project had to solve.</p>
        """,
    },
    {
        "slug": "wildlife-mapper",
        "file": "project-wildlife-mapper.html",
        "title": "Wildlife Mapper UAV",
        "eyebrow": "Personal Project",
        "status": "Active",
        "status_class": "active",
        "meta": "May 2025 — Present",
        "tags": ["Python", "YOLOv8", "Computer Vision", "UAV Systems", "GPS Integration"],
        "body": """
        <p>Wildlife Mapper UAV integrates a YOLOv8 computer vision model onto a UAV for real-time
        aerial wildlife detection, achieving 95% detection accuracy in field tests.</p>
        <h2>What I built</h2>
        <ul>
          <li>Integrated a YOLOv8 model onto UAV hardware for real-time aerial wildlife detection</li>
          <li>Built a full Python computer vision pipeline for onboard inference — from image
          capture through GPS-tagged detection logging</li>
          <li>Validated the system's detection accuracy through field testing, reaching 95%
          accuracy</li>
        </ul>
        <h2>Why it matters</h2>
        <p>Manual wildlife surveys are slow and labor-intensive. A UAV that can detect and
        geotag wildlife in real time, onboard, without needing to transmit raw video for
        after-the-fact analysis, makes large-area surveys far more practical.</p>
        """,
    },
]


def render_tags(tags):
    return "\n".join(f'  <span class="tag-pill">{t}</span>' for t in tags)


for i, p in enumerate(PROJECTS):
    prev_p = PROJECTS[i - 1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    html = TEMPLATE.format(
        title=p["title"],
        eyebrow=p["eyebrow"],
        status=p["status"],
        status_class=p["status_class"],
        meta=p["meta"],
        slug=p["slug"],
        tags=render_tags(p["tags"]),
        body=p["body"],
        nav=NAV,
        footer=FOOTER,
        prev_link=prev_p["file"],
        prev_title=prev_p["title"],
        next_link=next_p["file"],
        next_title=next_p["title"],
    )
    with open(p["file"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {p['file']}")
