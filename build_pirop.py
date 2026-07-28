# Master Build Script for PIROP Platform
# Generates fully standalone index.html and PIROP-Platform.html with inlined Chart.js, clean SVG icons, no emojis, and zero AI mentions.

import os

WORKDIR = r"C:\Users\Admin\.gemini\antigravity-ide\scratch\PIROP"
CHART_JS_PATH = os.path.join(WORKDIR, "chart.umd.min.js")

if not os.path.exists(CHART_JS_PATH):
    import urllib.request
    url = "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"
    urllib.request.urlretrieve(url, CHART_JS_PATH)

with open(CHART_JS_PATH, "r", encoding="utf-8") as f:
    chart_js_code = f.read()

PARTS = []

# Part 1: HTML Head + Inlined CSS + Inlined Chart.js
PARTS.append(r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PIROP &#8212; Enterprise Pricing Intelligence &amp; Revenue Optimization Platform</title>
<meta name="description" content="PIROP: Mada Media enterprise OOH pricing intelligence &#8212; benchmark-first pricing, financial feasibility, approvals, governance, commercial intelligence assistant.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<style>
:root{
  --ink:#0E1420;--ink-soft:#1B2436;--paper:#F5F6FA;--panel:#FFFFFF;
  --accent:#2F5EFF;--accent-dim:#4C6FFF;--accent-soft:#E9EDFF;
  --amber:#C6821F;--amber-soft:#FBF0DD;--green:#0F8A55;--green-soft:#E4F6EC;
  --red:#D33B3B;--red-soft:#FCE9E9;--line:#E3E6EE;--text-dim:#69707F;
  --radius:10px;--purple:#7C3AED;--purple-soft:#EDE9FE;
}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;}
body{background:var(--paper);color:var(--ink);font-family:'Inter',system-ui,-apple-system,sans-serif;font-size:14px;-webkit-font-smoothing:antialiased;}
h1,h2,h3,h4{font-family:'Space Grotesk',system-ui,sans-serif;margin:0;letter-spacing:-.01em;}
.mono{font-family:'IBM Plex Mono',monospace;}
button{font-family:'Inter',system-ui,sans-serif;cursor:pointer;}
input,select,textarea{font-family:'Inter',system-ui,sans-serif;}
::-webkit-scrollbar{width:8px;height:8px;}
::-webkit-scrollbar-thumb{background:#D5D9E3;border-radius:8px;}

/* LOGIN */
#login-screen{min-height:100vh;display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 20% 20%,#16203a 0%,var(--ink) 55%);position:relative;overflow:hidden;}
#login-screen::before{content:'';position:absolute;inset:0;background:radial-gradient(circle at 80% 80%,rgba(47,94,255,.06) 0%,transparent 60%);}
.login-card{width:440px;max-width:92vw;background:var(--panel);border-radius:20px;padding:40px 38px 32px;box-shadow:0 40px 100px rgba(0,0,0,.4);position:relative;z-index:1;animation:slideUp .4s cubic-bezier(.16,1,.3,1);}
@keyframes slideUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
.login-brand{display:flex;align-items:center;gap:14px;margin-bottom:8px;}
.brand-mark{width:38px;height:38px;border-radius:10px;background:var(--ink);display:flex;align-items:center;justify-content:center;position:relative;flex-shrink:0;}
.brand-mark:before{content:"";position:absolute;left:8px;bottom:8px;width:6px;height:13px;background:var(--accent-dim);border-radius:2px;}
.brand-mark:after{content:"";position:absolute;left:17px;bottom:8px;width:6px;height:21px;background:#fff;border-radius:2px;}
.login-brand h1{font-size:22px;}
.vbadge{font-size:11px;background:var(--accent-soft);color:var(--accent);padding:2px 8px;border-radius:20px;font-weight:600;}
.login-sub{color:var(--text-dim);font-size:13px;margin:2px 0 28px;line-height:1.6;}
.field{margin-bottom:18px;}
.field label{display:block;font-size:11.5px;font-weight:700;color:var(--text-dim);margin-bottom:7px;text-transform:uppercase;letter-spacing:.06em;}
.field input{width:100%;padding:11px 13px;border:1.5px solid var(--line);border-radius:9px;font-size:14px;background:#fff;transition:.15s;}
.field input:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft);}
.role-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
.role-opt{border:1.5px solid var(--line);border-radius:9px;padding:11px 12px;font-size:12.5px;text-align:left;background:#fff;transition:.15s;cursor:pointer;}
.role-opt:hover,.role-opt.active{border-color:var(--accent);background:var(--accent-soft);}
.role-opt.active{color:var(--accent);}
.role-opt b{display:block;font-size:13px;margin-bottom:2px;color:inherit;}
.role-opt span{color:var(--text-dim);font-size:11.5px;line-height:1.4;}
.btn-primary{width:100%;padding:13px;border:none;border-radius:9px;background:var(--ink);color:#fff;font-weight:700;font-size:14px;margin-top:22px;transition:.18s;}
.btn-primary:hover{background:var(--accent);transform:translateY(-1px);box-shadow:0 8px 20px rgba(47,94,255,.3);}
.login-foot{margin-top:18px;font-size:11.5px;color:var(--text-dim);text-align:center;}
.login-foot strong{color:var(--ink);}

/* APP SHELL */
#app{display:none;min-height:100vh;grid-template-columns:240px 1fr;}
#app.show{display:grid;}
.sidebar{background:var(--ink);color:#cbd2e6;padding:22px 16px;display:flex;flex-direction:column;position:sticky;top:0;height:100vh;overflow-y:auto;}
.side-brand{display:flex;align-items:center;gap:12px;padding:4px 8px 22px;border-bottom:1px solid rgba(255,255,255,.08);margin-bottom:16px;}
.side-brand .brand-mark{width:30px;height:30px;border-radius:8px;}
.side-brand span{font-family:'Space Grotesk',sans-serif;font-weight:700;color:#fff;font-size:16px;}
.nav-group-label{font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:rgba(255,255,255,.3);font-weight:700;padding:12px 12px 4px;margin-top:4px;}
.nav-item{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:8px;color:#aab2c8;font-size:13px;font-weight:500;margin-bottom:1px;transition:.12s;cursor:pointer;}
.nav-item:hover{background:rgba(255,255,255,.07);color:#fff;}
.nav-item.active{background:var(--accent);color:#fff;font-weight:600;}
.nav-icon{width:16px;height:16px;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;opacity:.85;}
.nav-item.active .nav-icon{opacity:1;}
.nav-badge{margin-left:auto;background:var(--amber);color:#fff;padding:1px 7px;border-radius:10px;font-size:10px;font-weight:700;}
.side-foot{margin-top:auto;padding-top:16px;border-top:1px solid rgba(255,255,255,.08);}
.role-pill{font-size:11px;background:rgba(255,255,255,.09);padding:7px 11px;border-radius:22px;display:flex;align-items:center;gap:6px;margin-bottom:10px;color:#fff;}
.role-pill-dot{width:7px;height:7px;border-radius:50%;background:var(--green);flex-shrink:0;}
.logout-btn{background:none;border:1px solid rgba(255,255,255,.18);color:#cbd2e6;padding:8px 12px;border-radius:8px;font-size:12px;width:100%;transition:.12s;}
.logout-btn:hover{border-color:rgba(255,255,255,.5);color:#fff;}

.main{padding:28px 36px 70px;overflow-y:auto;max-height:100vh;}
.topbar{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:24px;gap:16px;}
.topbar-left h2{font-size:23px;}
.topbar-left p{color:var(--text-dim);font-size:13px;margin-top:5px;}
.topbar-actions{display:flex;gap:8px;align-items:center;flex-shrink:0;flex-wrap:wrap;}

.chip{display:inline-flex;align-items:center;gap:5px;padding:4px 11px;border-radius:20px;font-size:11.5px;font-weight:600;}
.chip-blue{background:var(--accent-soft);color:var(--accent);}
.chip-green{background:var(--green-soft);color:var(--green);}
.chip-amber{background:var(--amber-soft);color:var(--amber);}
.chip-red{background:var(--red-soft);color:var(--red);}
.chip-grey{background:#EEF0F5;color:var(--text-dim);}
.chip-purple{background:var(--purple-soft);color:var(--purple);}

.grid{display:grid;gap:16px;}
.grid-4{grid-template-columns:repeat(4,1fr);}
.grid-3{grid-template-columns:repeat(3,1fr);}
.grid-2{grid-template-columns:repeat(2,1fr);}
@media(max-width:1280px){.grid-4{grid-template-columns:repeat(2,1fr);}.grid-3{grid-template-columns:1fr 1fr;}}
@media(max-width:900px){.grid-2,.grid-3,.grid-4{grid-template-columns:1fr;}}

.card{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:20px 22px;}
.card-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;}
.card-hover{transition:.15s;}
.card-hover:hover{box-shadow:0 4px 24px rgba(14,20,32,.08);transform:translateY(-1px);}
.kpi-card{position:relative;overflow:hidden;}
.kpi-card::before{content:'';position:absolute;top:-20px;right:-20px;width:80px;height:80px;border-radius:50%;background:var(--accent-soft);opacity:.5;}
.kpi-card .kpi-label{font-size:11.5px;color:var(--text-dim);font-weight:700;text-transform:uppercase;letter-spacing:.05em;position:relative;}
.kpi-card .kpi-value{font-family:'IBM Plex Mono',monospace;font-size:26px;font-weight:600;margin-top:10px;position:relative;}
.kpi-card .kpi-delta{font-size:12px;margin-top:6px;font-weight:600;}
.kpi-up{color:var(--green);}
.kpi-down{color:var(--red);}

table{width:100%;border-collapse:collapse;font-size:13px;}
th{text-align:left;font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--text-dim);padding:9px 11px;border-bottom:2px solid var(--line);font-weight:700;}
td{padding:11px 11px;border-bottom:1px solid #EEF0F5;vertical-align:middle;}
tr:last-child td{border-bottom:none;}
tr:hover td{background:#FAFBFD;}
.table-wrap{overflow-x:auto;}

.btn{padding:9px 15px;border-radius:8px;border:1.5px solid var(--line);background:#fff;font-size:13px;font-weight:600;color:var(--ink);transition:.14s;}
.btn:hover{border-color:var(--accent);color:var(--accent);background:var(--accent-soft);}
.btn-dark{background:var(--ink);color:#fff;border:none;}
.btn-dark:hover{background:var(--accent);transform:translateY(-1px);}
.btn-green{background:var(--green);color:#fff;border:none;}
.btn-green:hover{background:#0a7044;}
.btn-red{background:var(--red);color:#fff;border:none;}
.btn-red:hover{background:#b82e2e;}
.btn-sm{padding:5px 11px;font-size:12px;}
.btn:disabled{opacity:.4;cursor:not-allowed;pointer-events:none;}

.section-title{font-size:11.5px;text-transform:uppercase;letter-spacing:.07em;color:var(--text-dim);font-weight:700;margin-bottom:12px;}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;}
.form-row.full{grid-template-columns:1fr;}
.form-row.triple{grid-template-columns:1fr 1fr 1fr;}
.form-row label{display:block;font-size:11.5px;font-weight:700;color:var(--text-dim);margin-bottom:6px;text-transform:uppercase;letter-spacing:.04em;}
.form-row input,.form-row select,.form-row textarea{width:100%;padding:9px 11px;border:1.5px solid var(--line);border-radius:8px;font-size:13.5px;transition:.14s;background:#fff;}
.form-row input:focus,.form-row select:focus,.form-row textarea:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft);}
.form-row textarea{resize:vertical;min-height:64px;}

.confidence-wrap{margin:14px 0;}
.confidence-track{height:8px;border-radius:6px;background:linear-gradient(90deg,#EAB3B3 0%,#F0D28F 42%,#9FD8B6 100%);position:relative;}
.confidence-marker{position:absolute;top:-5px;width:3px;height:18px;background:var(--ink);border-radius:2px;}
.confidence-marker:after{content:attr(data-v);position:absolute;top:-24px;left:50%;transform:translateX(-50%);font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:700;white-space:nowrap;background:var(--ink);color:#fff;padding:2px 6px;border-radius:4px;}

.constellation{display:flex;align-items:center;justify-content:center;padding:6px 0;}
.rationale-box{background:linear-gradient(135deg,var(--accent-soft),#f0f4ff);border:1px solid #c5d0ff;border-radius:9px;padding:13px 15px;font-size:13px;color:#2C3557;margin-top:12px;line-height:1.6;}
.rationale-box b{color:var(--accent);}

.audit-item{border-left:2px solid var(--line);padding:9px 0 9px 16px;position:relative;margin-left:6px;}
.audit-item:before{content:"";position:absolute;left:-5px;top:16px;width:8px;height:8px;border-radius:50%;background:var(--accent);}
.audit-item b{font-size:13px;}
.audit-item div{font-size:12.5px;color:var(--text-dim);margin-top:2px;line-height:1.5;}
.audit-item .audit-meta{font-size:11px;color:var(--text-dim);margin-top:4px;}

.empty-state{text-align:center;padding:56px 20px;color:var(--text-dim);}
.empty-state .empty-icon{width:40px;height:40px;margin:0 auto 12px;display:flex;align-items:center;justify-content:center;background:var(--paper);border-radius:50%;color:var(--text-dim);}
.empty-state h3{color:var(--ink);margin-bottom:8px;font-size:16px;}
.empty-state p{font-size:13px;line-height:1.6;max-width:320px;margin:0 auto;}

.copilot-wrap{display:flex;flex-direction:column;height:calc(100vh - 180px);}
.copilot-log{flex:1;overflow-y:auto;padding:8px 4px 16px;}
.msg{max-width:80%;padding:12px 15px;border-radius:13px;font-size:13.5px;line-height:1.6;margin-bottom:10px;white-space:pre-wrap;animation:msgIn .2s ease;}
@keyframes msgIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.msg-user{background:var(--ink);color:#fff;margin-left:auto;border-bottom-right-radius:3px;}
.msg-ai{background:#fff;border:1px solid var(--line);margin-right:auto;border-bottom-left-radius:3px;box-shadow:0 2px 10px rgba(14,20,32,.06);}
.copilot-input{display:flex;gap:10px;padding-top:14px;border-top:1px solid var(--line);}
.copilot-input input{flex:1;padding:13px 15px;border-radius:10px;border:1.5px solid var(--line);font-size:14px;transition:.14s;}
.copilot-input input:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft);}
.suggestion-chips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px;}
.suggestion-chip{display:inline-flex;align-items:center;background:#fff;border:1.5px solid var(--line);padding:7px 13px;border-radius:20px;font-size:12px;color:var(--text-dim);cursor:pointer;transition:.14s;}
.suggestion-chip:hover{border-color:var(--accent);color:var(--accent);background:var(--accent-soft);}
.typing-dots span{display:inline-block;width:5px;height:5px;background:var(--text-dim);border-radius:50%;margin-right:3px;animation:blink 1.2s infinite ease-in-out;}
.typing-dots span:nth-child(2){animation-delay:.2s;}
.typing-dots span:nth-child(3){animation-delay:.4s;}
@keyframes blink{0%,80%,100%{opacity:.2}40%{opacity:1}}
.badge-source{font-size:10.5px;padding:3px 8px;border-radius:5px;background:#EEF0F5;color:var(--text-dim);font-weight:600;}
.loading-note{color:var(--text-dim);font-size:13px;padding:40px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:10px;}
.spinner{width:24px;height:24px;border:3px solid var(--line);border-top-color:var(--accent);border-radius:50%;animation:spin .8s linear infinite;}
@keyframes spin{to{transform:rotate(360deg)}}
.progress-bar-wrap{background:#EEF0F5;border-radius:6px;height:8px;overflow:hidden;}
.progress-bar-fill{height:100%;border-radius:6px;transition:width .5s ease;}
.scenario-card{border:1.5px solid var(--line);border-radius:10px;padding:16px;cursor:pointer;transition:.15s;background:#fff;}
.scenario-card:hover{border-color:var(--accent);box-shadow:0 4px 16px rgba(47,94,255,.1);}
.scenario-card.selected{border-color:var(--accent);background:var(--accent-soft);}
.insight-card{background:linear-gradient(135deg,#f8faff,#fff);border:1px solid var(--line);border-radius:10px;padding:16px;display:flex;gap:14px;align-items:flex-start;}
.insight-icon{width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:14px;font-weight:700;background:var(--accent-soft);color:var(--accent);}
.insight-body h4{font-size:13px;font-weight:700;margin-bottom:3px;}
.insight-body p{font-size:12.5px;color:var(--text-dim);line-height:1.5;margin:0;}
.phase-card{border-radius:12px;overflow:hidden;border:1px solid var(--line);}
.phase-header{padding:16px 20px;display:flex;align-items:center;gap:12px;}
.phase-num{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;flex-shrink:0;}
.phase-body{padding:16px 20px;background:#fff;}
.phase-item{display:flex;align-items:flex-start;gap:8px;margin-bottom:8px;font-size:13px;}
.phase-item:last-child{margin-bottom:0;}
.phase-dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;margin-top:6px;}
.timeline-bar{display:flex;gap:4px;margin-top:16px;}
.timeline-seg{height:6px;border-radius:3px;flex:1;}
.toast{position:fixed;bottom:28px;right:28px;background:var(--ink);color:#fff;padding:14px 20px;border-radius:10px;font-size:13.5px;font-weight:500;box-shadow:0 12px 40px rgba(0,0,0,.3);z-index:9999;animation:toastIn .3s cubic-bezier(.16,1,.3,1);max-width:360px;}
@keyframes toastIn{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
.toast-success{border-left:4px solid var(--green);}
.toast-error{border-left:4px solid var(--red);}
.toast-info{border-left:4px solid var(--accent);}
.modal-overlay{position:fixed;inset:0;background:rgba(14,20,32,.55);z-index:1000;display:flex;align-items:center;justify-content:center;backdrop-filter:blur(3px);animation:fadeIn .2s ease;}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.modal-box{background:#fff;border-radius:16px;padding:32px;max-width:560px;width:92vw;box-shadow:0 40px 100px rgba(0,0,0,.2);animation:slideUp .25s cubic-bezier(.16,1,.3,1);}
.modal-title{font-size:17px;font-weight:700;margin-bottom:6px;}
.modal-sub{font-size:13px;color:var(--text-dim);margin-bottom:22px;}
.modal-footer{display:flex;justify-content:flex-end;gap:8px;margin-top:22px;}
.filter-bar{display:flex;gap:8px;align-items:center;margin-bottom:16px;flex-wrap:wrap;}
.filter-bar select,.filter-bar input{padding:7px 11px;border:1.5px solid var(--line);border-radius:8px;font-size:13px;background:#fff;}
.filter-bar select:focus{outline:none;border-color:var(--accent);}
</style>

<!-- INLINED CHART.JS FOR MS TEAMS / OFFLINE / CSP COMPLIANCE -->
<script>
""")

PARTS.append(chart_js_code)

PARTS.append(r"""
</script>
</head>
<body>

<!-- LOGIN -->
<div id="login-screen">
  <div class="login-card">
    <div class="login-brand">
      <div class="brand-mark"></div>
      <h1>PIROP</h1>
      <span class="vbadge">v2.0</span>
    </div>
    <p class="login-sub">Enterprise Pricing Intelligence &amp; Revenue Optimization Platform<br><strong>Mada Media OOH Portfolio</strong></p>
    <div class="field">
      <label>Your Name</label>
      <input id="login-name" type="text" placeholder="e.g. Alok" value="Alok" autocomplete="off">
    </div>
    <div class="field">
      <label>Sign in as</label>
      <div class="role-grid" id="role-grid"></div>
    </div>
    <button class="btn-primary" onclick="doLogin()">Enter Platform &#8594;</button>
    <div class="login-foot">Demo environment &#183; Data persists locally &#183; <strong>No server required</strong></div>
  </div>
</div>

<!-- APP -->
<div id="app">
  <div class="sidebar">
    <div class="side-brand"><div class="brand-mark"></div><span>PIROP</span></div>
    <div id="nav"></div>
    <div class="side-foot">
      <div id="role-pill-wrap"></div>
      <button class="logout-btn" onclick="doLogout()">&#8644; Switch User</button>
    </div>
  </div>
  <div class="main" id="main"></div>
</div>

<script>
/* ================================================================
   PIROP v2.0 — Complete Enterprise Pricing Platform
   localStorage persistence | Smart local Commercial Intelligence
================================================================ */

const SVG_ICONS = {
  dashboard: `<svg class="nav-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h7"/></svg>`,
  insights: `<svg class="nav-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 8v8M8 12h8"/></svg>`,
  ppu: `<svg class="nav-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>`,
  assets: `<svg class="nav-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 9h6M9 13h6M9 17h4"/></svg>`,
  pricing: `<svg class="nav-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>`,
  scenario: `<svg class="nav-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M6 3v12s0 3 3 3h6m0 0l-3-3m3 3l-3 3M18 6a3 3 0 100-6 3 3 0 000 6zM6 21a3 3 0 100-6 3 3 0 000 6z"/></svg>`,
  finance_module: `<svg class="nav-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>`,
  approvals: `<svg class="nav-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>`,
  governance: `<svg class="nav-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>`,
  copilot: `<svg class="nav-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M8 10h.01M12 10h.01M16 10h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>`,
  roadmap: `<svg class="nav-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg>`
};

const ROLES=[
  {id:'analyst', label:'Pricing Analyst',    desc:'Create & run pricing recommendations'},
  {id:'finance', label:'Finance Manager',     desc:'Financial feasibility & MAG modelling'},
  {id:'approver',label:'Commercial Approver', desc:'Approve or reject pricing decisions'},
  {id:'exec',    label:'Executive',           desc:'Portfolio KPIs & strategic insights'},
  {id:'admin',   label:'Platform Admin',      desc:'Full access — manage PPU & assets'},
];
const NAV=[
  {id:'dashboard',     label:'Executive Dashboard',  icon:SVG_ICONS.dashboard,roles:['analyst','finance','approver','exec','admin'],group:'Overview'},
  {id:'insights',      label:'Market Insights',     icon:SVG_ICONS.insights,roles:['analyst','finance','exec','admin'],group:'Overview'},
  {id:'ppu',           label:'Price Point Universe', icon:SVG_ICONS.ppu,roles:['analyst','admin','finance'],group:'Pricing'},
  {id:'assets',        label:'Asset Catalogue',      icon:SVG_ICONS.assets,roles:['analyst','admin','finance'],group:'Pricing'},
  {id:'pricing',       label:'Pricing Workspace',    icon:SVG_ICONS.pricing,roles:['analyst','admin'],group:'Pricing'},
  {id:'scenario',      label:'Scenario Planning',    icon:SVG_ICONS.scenario,roles:['analyst','finance','admin'],group:'Pricing'},
  {id:'finance_module',label:'Financial Feasibility',icon:SVG_ICONS.finance_module,roles:['finance','admin','analyst'],group:'Finance'},
  {id:'approvals',     label:'Approvals Queue',      icon:SVG_ICONS.approvals,roles:['approver','admin'],group:'Workflow'},
  {id:'governance',    label:'Governance & Audit',   icon:SVG_ICONS.governance,roles:['analyst','finance','approver','exec','admin'],group:'Workflow'},
  {id:'copilot',       label:'Commercial Intelligence',icon:SVG_ICONS.copilot,roles:['analyst','finance','approver','exec','admin'],group:'Intelligence'},
  {id:'roadmap',       label:'Platform Roadmap',     icon:SVG_ICONS.roadmap,roles:['analyst','finance','approver','exec','admin'],group:'Intelligence'},
];

let state={user:null,role:'analyst',tab:'dashboard',assets:[],benchmarks:[],requests:[],audit:[],financialModels:[],scenarios:[],loaded:false};

function lsGet(k){try{const v=localStorage.getItem(k);return v?JSON.parse(v):null;}catch(e){return null;}}
function lsSet(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){console.warn(e);}}
function saveAll(){lsSet('pirop_a',state.assets);lsSet('pirop_b',state.benchmarks);lsSet('pirop_r',state.requests);lsSet('pirop_au',state.audit);lsSet('pirop_f',state.financialModels);lsSet('pirop_s',state.scenarios);}
function saveReqs(){lsSet('pirop_r',state.requests);}
function saveBMs(){lsSet('pirop_b',state.benchmarks);}
function saveAudit(){lsSet('pirop_au',state.audit);}
function saveFin(){lsSet('pirop_f',state.financialModels);}
function saveScen(){lsSet('pirop_s',state.scenarios);}

function logAudit(action,entity,details){
  state.audit.unshift({id:'AUD-'+Date.now().toString(36).toUpperCase(),ts:new Date().toISOString(),actor:(state.user||'System')+' ('+roleLabel(state.role)+')',action,entity,details});
  saveAudit();
}
function roleLabel(id){const r=ROLES.find(x=>x.id===id);return r?r.label:id;}

/* Safe Chart creation */
function createSafeChart(canvasId, config){
  const el = document.getElementById(canvasId);
  if (!el) return;
  if (typeof Chart === 'undefined') {
    const p = el.parentElement;
    if (p) {
      p.innerHTML += '<div style="padding:20px;text-align:center;color:var(--text-dim);font-size:12px;">Chart visualization unavailable</div>';
    }
    return;
  }
  try {
    new Chart(el, config);
  } catch(e) {
    console.error('Chart error on ' + canvasId, e);
  }
}

function loadAll(){
  const a=lsGet('pirop_a');
  if(!a){seedData();return;}
  state.assets=a;state.benchmarks=lsGet('pirop_b')||[];state.requests=lsGet('pirop_r')||[];
  state.audit=lsGet('pirop_au')||[];state.financialModels=lsGet('pirop_f')||[];state.scenarios=lsGet('pirop_s')||[];
  state.loaded=true;
}

function seedData(){
  const rows=[
    ['DB-NM-014','North Metro','Digital Billboard',82000,61,1.8],
    ['SB-SC-027','South Corridor','Static Billboard',41000,38,2.4],
    ['TS-EM-009','East Transit Hub','Transit Shelter',65000,74,0.6],
    ['MD-WB-003','West Business District','Mall Digital Screen',29000,55,1.2],
    ['HG-NM-041','North Metro','Highway Gantry',118000,47,3.6],
    ['DB-WB-018','West Business District','Digital Billboard',96000,69,2.1],
    ['SB-EM-011','East Transit Hub','Static Billboard',33000,42,1.5],
    ['TS-SC-022','South Corridor','Transit Shelter',58000,66,0.5],
    ['DB-SC-005','South Corridor','Digital Billboard',74000,58,2.0],
    ['HG-WB-030','West Business District','Highway Gantry',105000,51,3.2],
    ['MD-NM-007','North Metro','Mall Digital Screen',44000,63,0.9],
    ['TS-NM-016','North Metro','Transit Shelter',71000,49,0.7],
  ];
  state.assets=rows.map(([code,region,cls,traffic,occ,size],i)=>({
    id:'AST-'+String(i+1).padStart(3,'0'),code,region,assetClass:cls,
    trafficVolume:traffic,audienceReach:Math.round(traffic*0.62),
    occupancy:occ,sizeSqm:size,
    status:occ>60?'High Demand':occ>40?'Available':'Low Demand',
    lastUpdated:new Date(Date.now()-i*3*864e5).toISOString().slice(0,10)
  }));
  const srcs=['Investor Rate Card','Mystery Shopping','Historical Contract','Approved Contract'];
  state.benchmarks=[];
  state.assets.forEach((a,i)=>{
    if(i%3!==2){
      const base=8+(a.trafficVolume/10000)+(a.occupancy/10);
      state.benchmarks.push({
        id:'PPU-'+String(i+1).padStart(3,'0'),
        assetClass:a.assetClass,region:a.region,
        pricePerDay:Math.round(base*95),
        source:srcs[i%srcs.length],
        capturedOn:new Date(Date.now()-i*5*864e5).toISOString().slice(0,10),
        note:'Reference for '+a.assetClass+' in '+a.region,
        confidence:75+Math.round(Math.random()*20)
      });
    }
  });
  const seedR=[
    {ai:0,cust:'Nova Beverages Pvt Ltd',dur:30,st:'Approved',cf:88,mth:'Benchmark Match'},
    {ai:2,cust:'TechCorp Innovations',dur:14,st:'Approved',cf:82,mth:'Benchmark Match'},
    {ai:4,cust:'SkyLine Retail',dur:60,st:'Rejected',cf:55,mth:'Intelligent Fallback'},
    {ai:1,cust:'BlueStar Finance',dur:45,st:'Pending Approval',cf:71,mth:'Benchmark Match'},
    {ai:5,cust:'GreenLeaf Foods',dur:21,st:'Approved',cf:91,mth:'Benchmark Match'},
    {ai:3,cust:'UrbanFit Gym Chain',dur:30,st:'Pending Approval',cf:62,mth:'Intelligent Fallback'},
  ];
  state.requests=seedR.map((r,i)=>{
    const ast=state.assets[r.ai];
    const eng=runPricingEngine(ast,r.dur);
    const fp=Math.round(eng.suggestedPrice*(0.95+Math.random()*0.1));
    return {
      id:'PR-'+String(1001+i),assetId:ast.id,customer:r.cust,duration:r.dur,
      method:r.mth,confidence:r.cf,suggestedPrice:eng.suggestedPrice,finalPrice:fp,
      status:r.st,notes:'',createdBy:'System',
      createdAt:new Date(Date.now()-i*4*864e5).toISOString(),
      rationale:eng.rationale,
      decidedBy:r.st!=='Pending Approval'?'System':null,
      decidedAt:r.st!=='Pending Approval'?new Date(Date.now()-i*3*864e5).toISOString():null,
      decisionComment:''
    };
  });
  state.scenarios=[
    {id:'SCN-001',name:'Base Case',description:'Current rate card, no adjustment',occupancyTarget:55,discountCap:10,priceAdjustment:0,createdAt:new Date().toISOString()},
    {id:'SCN-002',name:'Aggressive Growth',description:'Price reduction to capture share',occupancyTarget:72,discountCap:20,priceAdjustment:-12,createdAt:new Date().toISOString()},
    {id:'SCN-003',name:'Premium Positioning',description:'Rate increase on high-demand assets',occupancyTarget:48,discountCap:5,priceAdjustment:18,createdAt:new Date().toISOString()},
  ];
  state.financialModels=[];
  state.audit=[{id:'AUD-INIT',ts:new Date().toISOString(),actor:'System',action:'Platform Initialized',entity:'PIROP',details:'Seeded '+state.benchmarks.length+' benchmarks, '+state.assets.length+' assets, '+state.requests.length+' demo requests.'}];
  state.loaded=true;
  saveAll();
}

/* ---- PRICING ENGINE ---- */
function matchBMs(asset){return state.benchmarks.filter(b=>b.assetClass===asset.assetClass&&b.region===asset.region);}
function runPricingEngine(asset,days){
  const m=matchBMs(asset);
  if(m.length>0){
    const avg=m.reduce((s,x)=>s+x.pricePerDay,0)/m.length;
    const recent=m.some(x=>(Date.now()-new Date(x.capturedOn))/864e5<60);
    const conf=Math.min(96,62+m.length*8+(recent?8:0));
    return {method:'Benchmark Match',confidence:conf,suggestedPrice:Math.round(avg*days),dailyRate:Math.round(avg),comparables:m,
      rationale:'Matched against '+m.length+' PPU record'+(m.length>1?'s':'')+' for '+asset.assetClass+' in '+asset.region+'. Average benchmark INR '+Math.round(avg).toLocaleString('en-IN')+'/day from '+[...new Set(m.map(x=>x.source))].join(', ')+'. Benchmark-first policy applied per PPU governance.'
    };
  }
  const sim=state.assets.filter(a=>a.id!==asset.id)
    .map(a=>({a,score:1/(1+Math.abs(a.trafficVolume-asset.trafficVolume)/20000+Math.abs(a.occupancy-asset.occupancy)/40)}))
    .sort((x,y)=>y.score-x.score).slice(0,3);
  const tf=asset.trafficVolume/1000,rf=asset.audienceReach/1000,of=asset.occupancy/100;
  const dr=Math.round((tf*3.1+rf*1.4)*(0.55+of));
  const conf=Math.min(70,40+Math.round(of*20)+sim.length*3);
  return {method:'Intelligent Fallback',confidence:conf,suggestedPrice:dr*days,dailyRate:dr,
    comparables:sim.map(s=>({assetClass:s.a.assetClass,region:s.a.region,pricePerDay:'~',source:'Similar: '+s.a.code})),
    rationale:'No PPU benchmark for '+asset.assetClass+' in '+asset.region+'. Fallback engine used traffic ('+asset.trafficVolume.toLocaleString()+'), reach ('+asset.audienceReach.toLocaleString()+'), occupancy ('+asset.occupancy+'%) and '+sim.length+' comparable assets by similarity score. Confidence capped — human review required.'
  };
}
function financialFeasibility({revenueTotal,costTotal,years,discountRate,revenueSharePct,mag}){
  const ar=revenueTotal/years,ac=costTotal/years;
  const cfs=Array.from({length:years},()=>ar-ac);
  const roi=costTotal>0?((revenueTotal-costTotal)/costTotal)*100:0;
  let npv=-costTotal;cfs.forEach((cf,i)=>{npv+=cf/Math.pow(1+discountRate/100,i+1);});
  const npvAt=r=>{let v=-costTotal;cfs.forEach((cf,i)=>{v+=cf/Math.pow(1+r,i+1);});return v;};
  let lo=-0.9,hi=5,irr=0;
  for(let it=0;it<100;it++){const mid=(lo+hi)/2;const v=npvAt(mid);if(Math.abs(v)<0.5){irr=mid;break;}v>0?lo=mid:hi=mid;irr=mid;}
  let cum=-costTotal,payback=null;
  for(let i=0;i<years;i++){cum+=cfs[i];if(cum>=0&&payback===null)payback=i+(1-cum/cfs[i]);}
  const rsa=revenueTotal*(revenueSharePct/100);
  return {roi,npv,irr:irr*100,payback,revenueShareAmt:rsa,guaranteedTake:Math.max(mag*years,rsa),annualRevenue:ar,annualCost:ac,breakevenOcc:costTotal>0?Math.round(ac/ar*100):0,cashFlows:cfs};
}

/* ---- VISUALS ---- */
function confidenceMeter(conf){
  const clr=conf>=75?'var(--green)':conf>=50?'var(--amber)':'var(--red)';
  return `<div class="confidence-wrap"><div style="display:flex;justify-content:space-between;font-size:11px;color:var(--text-dim);margin-bottom:8px;"><span>LOW</span><span style="font-weight:700;color:${clr};">${conf}%</span><span>HIGH CONFIDENCE</span></div><div class="confidence-track"><div class="confidence-marker" style="left:calc(${conf}% - 1px);" data-v="${conf}%"></div></div></div>`;
}
function constellationSVG(cl,comps){
  const cx=155,cy=115,R=76,n=Math.max(comps.length,1);let nd='';
  comps.forEach((c,i)=>{
    const a=(Math.PI*2*i/n)-Math.PI/2,x=cx+R*Math.cos(a),y=cy+R*Math.sin(a);
    const lb=(c.source?c.source.split(':')[0]:'BM').substring(0,14);
    const vl=typeof c.pricePerDay==='number'?'INR'+Math.round(c.pricePerDay/1000)+'k':'ref';
    nd+=`<line x1="${cx}" y1="${cy}" x2="${x}" y2="${y}" stroke="#B9C4FF" stroke-width="1.5" stroke-dasharray="4 3"/><circle cx="${x}" cy="${y}" r="22" fill="#E9EDFF" stroke="#2F5EFF" stroke-width="1.5"/><text x="${x}" y="${y+4}" text-anchor="middle" font-size="9" font-family="IBM Plex Mono,monospace" fill="#2F5EFF" font-weight="700">${vl}</text><text x="${x}" y="${y+38}" text-anchor="middle" font-size="9" font-family="Inter,sans-serif" fill="#69707F">${lb}</text>`;
  });
  return `<svg viewBox="0 0 310 250" width="100%" height="220"><circle cx="${cx}" cy="${cy}" r="28" fill="#0E1420"/><text x="${cx}" y="${cy-4}" text-anchor="middle" font-size="9" font-family="Space Grotesk,sans-serif" fill="#aab2c8">ASSET</text><text x="${cx}" y="${cy+9}" text-anchor="middle" font-size="10" font-family="Space Grotesk,sans-serif" fill="#fff" font-weight="700">${cl}</text>${nd}</svg>`;
}
function statusChip(s){const m={'Draft':'chip-grey','Pending Approval':'chip-amber','Approved':'chip-green','Rejected':'chip-red'};return `<span class="chip ${m[s]||'chip-grey'}">${s}</span>`;}
function emptyState(title,sub){return `<div class="empty-state"><h3>${title}</h3><p>${sub}</p></div>`;}
function progressBar(pct,color='var(--accent)'){return `<div class="progress-bar-wrap"><div class="progress-bar-fill" style="width:${Math.min(pct,100)}%;background:${color};"></div></div>`;}
function showToast(msg,type='info',dur=3200){
  const t=document.createElement('div');t.className='toast toast-'+type;t.textContent=msg;document.body.appendChild(t);
  setTimeout(()=>{t.style.opacity='0';t.style.transition='opacity .3s';setTimeout(()=>t.remove(),320);},dur);
}

/* ---- LOGIN / LOGOUT ---- */
function renderRoleGrid(){
  document.getElementById('role-grid').innerHTML=ROLES.map(r=>`<button type="button" class="role-opt ${r.id==='analyst'?'active':''}" data-role="${r.id}" onclick="selectRole('${r.id}')"><b>${r.label}</b><span>${r.desc}</span></button>`).join('');
}
let selectedRole='analyst';
function selectRole(id){selectedRole=id;document.querySelectorAll('.role-opt').forEach(b=>b.classList.toggle('active',b.dataset.role===id));}
function doLogin(){
  const name=document.getElementById('login-name').value.trim()||'Guest';
  state.user=name;state.role=selectedRole;
  document.getElementById('login-screen').style.display='none';
  document.getElementById('app').classList.add('show');
  document.getElementById('main').innerHTML='<div class="loading-note"><div class="spinner"></div>Loading Price Point Universe&hellip;</div>';
  loadAll();
  logAudit('User Signed In','Session',name+' signed in as '+roleLabel(state.role));
  renderNav();goTab('dashboard');
}
function doLogout(){document.getElementById('app').classList.remove('show');document.getElementById('login-screen').style.display='flex';copilotHistory=[];}

/* ---- NAV ---- */
function renderNav(){
  const el=document.getElementById('nav');
  const acc=NAV.filter(n=>n.roles.includes(state.role));
  const groups=[...new Set(acc.map(n=>n.group))];
  el.innerHTML=groups.map(g=>`<div class="nav-group-label">${g}</div>${acc.filter(n=>n.group===g).map(n=>`<div class="nav-item ${state.tab===n.id?'active':''}" onclick="goTab('${n.id}')">${n.icon} ${n.label}${n.id==='approvals'?`<span class="nav-badge">${state.requests.filter(r=>r.status==='Pending Approval').length||''}</span>`:''}</div>`).join('')}`).join('');
  document.getElementById('role-pill-wrap').innerHTML=`<div class="role-pill"><div class="role-pill-dot"></div>${state.user} &middot; ${roleLabel(state.role)}</div>`;
}
function goTab(id){state.tab=id;renderNav();renderMain();document.querySelector('.main')?.scrollTo(0,0);}
function renderMain(){
  const m=document.getElementById('main');
  const R={dashboard:renderDashboard,insights:renderInsights,ppu:renderPPU,assets:renderAssets,pricing:renderPricing,scenario:renderScenario,finance_module:renderFinanceModule,approvals:renderApprovals,governance:renderGovernance,copilot:renderCopilot,roadmap:renderRoadmap};
  m.innerHTML='';(R[state.tab]||renderDashboard)(m);
}

/* ---- DASHBOARD ---- */
function renderDashboard(m){
  const reqs=state.requests,approved=reqs.filter(r=>r.status==='Approved'),pending=reqs.filter(r=>r.status==='Pending Approval'),rejected=reqs.filter(r=>r.status==='Rejected');
  const totalRev=approved.reduce((s,r)=>s+(r.finalPrice||0),0);
  const avgOcc=state.assets.length?Math.round(state.assets.reduce((s,a)=>s+a.occupancy,0)/state.assets.length):0;
  const winRate=reqs.length?Math.round(100*approved.length/reqs.length):0;
  const asp=approved.length?Math.round(totalRev/approved.length):0;
  const rBR={};state.assets.forEach(a=>{rBR[a.region]=rBR[a.region]||0;});
  approved.forEach(r=>{const a=state.assets.find(x=>x.id===r.assetId);if(a)rBR[a.region]=(rBR[a.region]||0)+(r.finalPrice||0);});
  const oBCls={};state.assets.forEach(a=>{if(!oBCls[a.assetClass])oBCls[a.assetClass]={s:0,c:0};oBCls[a.assetClass].s+=a.occupancy;oBCls[a.assetClass].c++;});
  const months=['Feb','Mar','Apr','May','Jun','Jul'];
  const mRev=months.map(()=>Math.max(0,Math.round(totalRev/6*(0.6+Math.random()*0.8))));
  mRev[5]=totalRev>0?Math.round(totalRev*0.22):0;

  m.innerHTML=`
    <div class="topbar">
      <div class="topbar-left"><h2>Executive Dashboard</h2><p>Portfolio-wide commercial KPIs across the Mada Media OOH asset base</p></div>
      <div class="topbar-actions"><span class="chip chip-blue">${state.assets.length} Assets</span><span class="chip chip-green">${state.benchmarks.length} Benchmarks</span><span class="chip chip-grey">${new Date().toLocaleDateString('en-IN',{day:'2-digit',month:'short',year:'numeric'})}</span></div>
    </div>
    <div class="grid grid-4" style="margin-bottom:18px;">
      <div class="card kpi-card card-hover"><div class="kpi-label">Realized Revenue</div><div class="kpi-value">&#8377;${totalRev.toLocaleString('en-IN')}</div><div class="kpi-delta kpi-up">&uarr; ${approved.length} approved deals</div></div>
      <div class="card kpi-card card-hover"><div class="kpi-label">Portfolio Occupancy</div><div class="kpi-value">${avgOcc}%</div><div class="kpi-delta ${avgOcc>=55?'kpi-up':'kpi-down'}">${avgOcc>=55?'&uarr; Above':'&darr; Below'} 55% target</div><div style="margin-top:8px;">${progressBar(avgOcc,avgOcc>=55?'var(--green)':'var(--amber)')}</div></div>
      <div class="card kpi-card card-hover"><div class="kpi-label">Win Rate</div><div class="kpi-value">${winRate}%</div><div class="kpi-delta">${reqs.length} total &middot; ${pending.length} pending</div><div style="margin-top:8px;">${progressBar(winRate,'var(--accent)')}</div></div>
      <div class="card kpi-card card-hover"><div class="kpi-label">Avg Selling Price</div><div class="kpi-value">&#8377;${asp.toLocaleString('en-IN')}</div><div class="kpi-delta">${rejected.length} rejected</div></div>
    </div>
    <div class="grid grid-2" style="margin-bottom:18px;">
      <div class="card"><div class="section-title">Revenue by Region</div><canvas id="cR" height="200"></canvas></div>
      <div class="card"><div class="section-title">Pipeline Status</div><canvas id="cS" height="200"></canvas></div>
    </div>
    <div class="grid grid-2" style="margin-bottom:18px;">
      <div class="card"><div class="section-title">Avg Occupancy by Asset Class</div><canvas id="cO" height="180"></canvas></div>
      <div class="card"><div class="section-title">Revenue Trend (6 Months)</div><canvas id="cT" height="180"></canvas></div>
    </div>
    <div class="card">
      <div class="card-header"><div class="section-title" style="margin-bottom:0;">Recent Pricing Activity</div><button class="btn btn-sm" onclick="goTab('pricing')">+ New</button></div>
      ${reqs.length===0?emptyState('No requests yet','Create one in Pricing Workspace.'):reqTable(reqs.slice(0,8))}
    </div>`;

  const rL=Object.keys(rBR);
  createSafeChart('cR',{type:'bar',data:{labels:rL,datasets:[{label:'Revenue',data:rL.map(k=>rBR[k]),backgroundColor:['#2F5EFF','#4C6FFF','#7B93FF','#A0B0FF'],borderRadius:6}]},options:{plugins:{legend:{display:false}},scales:{y:{grid:{color:'#EEF0F5'},ticks:{callback:v=>'INR'+Math.round(v/1000)+'k'}},x:{grid:{display:false}}}}});
  
  const sc={};reqs.forEach(r=>{sc[r.status]=(sc[r.status]||0)+1;});
  const sL=Object.keys(sc).length?Object.keys(sc):['No Data'],sD=Object.keys(sc).length?Object.values(sc):[1];
  createSafeChart('cS',{type:'doughnut',data:{labels:sL,datasets:[{data:sD,backgroundColor:['#0F8A55','#C6821F','#D33B3B','#E3E6EE'],hoverOffset:6}]},options:{plugins:{legend:{position:'bottom',labels:{boxWidth:10,font:{size:11},padding:12}}},cutout:'60%'}});
  
  const oL=Object.keys(oBCls),oV=oL.map(k=>Math.round(oBCls[k].s/oBCls[k].c));
  createSafeChart('cO',{type:'bar',data:{labels:oL,datasets:[{data:oV,backgroundColor:oV.map(v=>v>=60?'#0F8A55':v>=45?'#C6821F':'#D33B3B'),borderRadius:5}]},options:{plugins:{legend:{display:false}},scales:{y:{max:100,grid:{color:'#EEF0F5'},ticks:{callback:v=>v+'%'}},x:{grid:{display:false}}}}});
  
  createSafeChart('cT',{type:'line',data:{labels:months,datasets:[{data:mRev,borderColor:'#2F5EFF',backgroundColor:'rgba(47,94,255,.08)',tension:.35,fill:true,pointRadius:4,pointBackgroundColor:'#2F5EFF'}]},options:{plugins:{legend:{display:false}},scales:{y:{grid:{color:'#EEF0F5'},ticks:{callback:v=>'INR'+Math.round(v/1000)+'k'}},x:{grid:{display:false}}}}});
}
function reqTable(list){
  return `<div class="table-wrap"><table><thead><tr><th>Request</th><th>Asset</th><th>Customer</th><th>Method</th><th>Conf.</th><th>Price</th><th>Status</th></tr></thead><tbody>
    ${list.map(r=>{const a=state.assets.find(x=>x.id===r.assetId);const cc=r.confidence>=75?'var(--green)':r.confidence>=50?'var(--amber)':'var(--red)';return `<tr><td class="mono" style="font-weight:600;">${r.id}</td><td>${a?`<b>${a.code}</b><br><small style="color:var(--text-dim)">${a.assetClass}</small>`:'—'}</td><td>${r.customer}</td><td><span class="badge-source">${r.method==='Benchmark Match'?'Benchmark':'Fallback'}</span></td><td style="font-weight:700;color:${cc};">${r.confidence}%</td><td class="mono" style="font-weight:600;">&#8377;${(r.finalPrice||r.suggestedPrice||0).toLocaleString('en-IN')}</td><td>${statusChip(r.status)}</td></tr>`;}).join('')}
  </tbody></table></div>`;
}

/* ---- AI INSIGHTS ---- */
function renderInsights(m){
  const approved=state.requests.filter(r=>r.status==='Approved');
  const hi=state.assets.filter(a=>a.occupancy>=65),lo=state.assets.filter(a=>a.occupancy<40);
  const avgOcc=state.assets.length?Math.round(state.assets.reduce((s,a)=>s+a.occupancy,0)/state.assets.length):0;
  const fb=state.requests.filter(r=>r.method==='Intelligent Fallback');
  const wr=state.requests.length?Math.round(100*approved.length/state.requests.length):0;
  const uncov=state.assets.filter(a=>matchBMs(a).length===0);
  const pending=state.requests.filter(r=>r.status==='Pending Approval');
  const insights=[
    {code:'01',title:'Revenue Realization Opportunity',body:`${hi.length} assets above 65% occupancy — ${hi.map(a=>a.code).join(', ')}. A 12–18% rate uplift captures pricing premium without volume risk.`},
    {code:'02',title:'Underperforming Assets',body:lo.length===0?'All assets are above 40% occupancy — portfolio health is positive.':lo.length+' asset'+(lo.length!==1?'s':'')+' below 40% occupancy: '+lo.map(a=>a.code).join(', ')+'. Consider promotional bundling or 10–15% rate reduction.'},
    {code:'03',title:'PPU Coverage Gap',body:uncov.length===0?'Full benchmark coverage — all assets have PPU records.':uncov.length+' asset'+(uncov.length!==1?'s lack':' lacks')+' PPU benchmarks: '+uncov.map(a=>a.code).join(', ')+'. Adding these raises confidence and removes fallback dependency.'},
    {code:'04',title:'Occupancy vs. Target',body:`Portfolio average is ${avgOcc}% vs. 55% strategic target. ${avgOcc>=55?'The '+Math.abs(avgOcc-55)+' pp surplus above target creates pricing headroom.':'The '+Math.abs(avgOcc-55)+' pp shortfall represents unbooked inventory leakage.'}`},
    {code:'05',title:'Approval Queue Health',body:`${pending.length} request${pending.length!==1?'s are':' is'} pending. ${pending.filter(r=>r.method==='Intelligent Fallback').length} are fallback-priced — governance requires sign-off within 24 hours.`},
    {code:'06',title:'Win Rate Analysis',body:`Current win rate ${wr}% across ${state.requests.length} requests. Benchmark-matched deals close at significantly higher rates than fallback-priced deals — PPU expansion is the top commercial priority.`},
  ];
  m.innerHTML=`
    <div class="topbar"><div class="topbar-left"><h2>Market Insights</h2><p>Automated portfolio intelligence derived from live pricing data, occupancy signals and benchmark coverage</p></div><div class="topbar-actions"><span class="chip chip-purple">Auto-refreshed</span></div></div>
    <div class="grid grid-2">${insights.map(ins=>`<div class="insight-card card-hover"><div class="insight-icon">${ins.code}</div><div class="insight-body"><h4>${ins.title}</h4><p>${ins.body}</p></div></div>`).join('')}</div>`;
}

/* ---- PPU ---- */
function renderPPU(m){
  const canEdit=['admin','analyst'].includes(state.role);
  m.innerHTML=`
    <div class="topbar"><div class="topbar-left"><h2>Price Point Universe</h2><p>Master benchmark repository — the authoritative source of reference rates for all OOH pricing decisions</p></div><div class="topbar-actions">${canEdit?'<button class="btn btn-dark" onclick="openBMForm()">+ Add Benchmark</button>':''}<span class="chip chip-blue">${state.benchmarks.length} Records</span></div></div>
    <div id="ppu-slot"></div>
    <div class="filter-bar">
      <select id="pf-cls" onchange="renderPPUTable()"><option value="">All Classes</option>${[...new Set(state.assets.map(a=>a.assetClass))].map(c=>`<option>${c}</option>`).join('')}</select>
      <select id="pf-reg" onchange="renderPPUTable()"><option value="">All Regions</option>${[...new Set(state.assets.map(a=>a.region))].map(r=>`<option>${r}</option>`).join('')}</select>
      <select id="pf-src" onchange="renderPPUTable()"><option value="">All Sources</option><option>Investor Rate Card</option><option>Mystery Shopping</option><option>Historical Contract</option><option>Approved Contract</option></select>
    </div>
    <div class="card"><div id="ppu-table"></div></div>`;
  renderPPUTable();
}
function renderPPUTable(){
  const fc=document.getElementById('pf-cls')?.value||'',fr=document.getElementById('pf-reg')?.value||'',fs=document.getElementById('pf-src')?.value||'';
  const fl=state.benchmarks.filter(b=>(!fc||b.assetClass===fc)&&(!fr||b.region===fr)&&(!fs||b.source===fs));
  const el=document.getElementById('ppu-table');if(!el)return;
  if(!fl.length){el.innerHTML=emptyState('No records match','Adjust the filters above.');return;}
  el.innerHTML=`<div class="table-wrap"><table><thead><tr><th>ID</th><th>Class</th><th>Region</th><th>Rate/Day</th><th>Source</th><th>Captured</th><th>Confidence</th></tr></thead><tbody>
    ${fl.map(b=>{const cc=(b.confidence||80)>=80?'var(--green)':(b.confidence||80)>=60?'var(--amber)':'var(--red)';return `<tr><td class="mono" style="font-weight:600;">${b.id}</td><td>${b.assetClass}</td><td>${b.region}</td><td class="mono" style="font-weight:700;">&#8377;${b.pricePerDay.toLocaleString('en-IN')}</td><td><span class="badge-source">${b.source}</span></td><td class="mono">${b.capturedOn}</td><td style="font-weight:700;color:${cc};">${b.confidence||80}%</td></tr>`;}).join('')}
  </tbody></table></div>`;
}
function openBMForm(){
  const slot=document.getElementById('ppu-slot');
  const cls=[...new Set(state.assets.map(a=>a.assetClass))],reg=[...new Set(state.assets.map(a=>a.region))];
  slot.innerHTML=`<div class="card" style="margin-bottom:16px;border-color:var(--accent);"><div class="section-title">New Benchmark Record</div>
    <div class="form-row"><div><label>Asset Class</label><select id="bf-cls">${cls.map(c=>`<option>${c}</option>`).join('')}</select></div><div><label>Region</label><select id="bf-reg">${reg.map(r=>`<option>${r}</option>`).join('')}</select></div></div>
    <div class="form-row"><div><label>Rate/Day (&#8377;)</label><input id="bf-rate" type="number" placeholder="e.g. 7200" min="100"></div><div><label>Source</label><select id="bf-src"><option>Investor Rate Card</option><option>Mystery Shopping</option><option>Historical Contract</option><option>Approved Contract</option></select></div></div>
    <div class="form-row full"><div><label>Notes</label><textarea id="bf-note" placeholder="Context about this benchmark..."></textarea></div></div>
    <div style="display:flex;gap:8px;"><button class="btn btn-dark" onclick="submitBM()">Save Benchmark</button><button class="btn" onclick="document.getElementById('ppu-slot').innerHTML=''">Cancel</button></div>
  </div>`;
  slot.scrollIntoView({behavior:'smooth',block:'start'});
}
function submitBM(){
  const rate=parseFloat(document.getElementById('bf-rate').value);
  if(!rate||rate<=0){showToast('Enter a valid daily rate','error');return;}
  const b={id:'PPU-'+String(state.benchmarks.length+1).padStart(3,'0'),assetClass:document.getElementById('bf-cls').value,region:document.getElementById('bf-reg').value,pricePerDay:rate,source:document.getElementById('bf-src').value,capturedOn:new Date().toISOString().slice(0,10),note:document.getElementById('bf-note').value||'Manually added',confidence:82};
  state.benchmarks.unshift(b);saveBMs();
  logAudit('Benchmark Added','PPU',b.id+' — '+b.assetClass+'/'+b.region+' @ INR '+rate+'/day ('+b.source+')');
  document.getElementById('ppu-slot').innerHTML='';renderPPUTable();showToast(b.id+' saved','success');
}

/* ---- ASSETS ---- */
function renderAssets(m){
  const canManage=state.role==='admin';
  m.innerHTML=`
    <div class="topbar"><div class="topbar-left"><h2>Asset Catalogue</h2><p>Full OOH inventory — ${state.assets.length} assets across 4 regions and 5 asset classes</p></div><div class="topbar-actions">${canManage?'<button class="btn btn-dark" onclick="openAssetForm()">+ Add Asset</button>':''}<span class="chip chip-blue">${state.assets.length} Assets</span></div></div>
    <div id="af-slot"></div>
    <div class="grid grid-4" style="margin-bottom:18px;">
      ${[...new Set(state.assets.map(a=>a.assetClass))].slice(0,4).map(cls=>{const items=state.assets.filter(a=>a.assetClass===cls);const ao=items.length?Math.round(items.reduce((s,a)=>s+a.occupancy,0)/items.length):0;return `<div class="card kpi-card card-hover"><div class="kpi-label">${cls}</div><div class="kpi-value">${items.length}</div><div class="kpi-delta">Avg occ: ${ao}%</div><div style="margin-top:8px;">${progressBar(ao,ao>=60?'var(--green)':'var(--amber)')}</div></div>`;}).join('')}
    </div>
    <div class="card">
      <div class="filter-bar">
        <select id="af-reg" onchange="renderAssetTable()"><option value="">All Regions</option>${[...new Set(state.assets.map(a=>a.region))].map(r=>`<option>${r}</option>`).join('')}</select>
        <select id="af-cls" onchange="renderAssetTable()"><option value="">All Classes</option>${[...new Set(state.assets.map(a=>a.assetClass))].map(c=>`<option>${c}</option>`).join('')}</select>
        <select id="af-st" onchange="renderAssetTable()"><option value="">All Statuses</option><option>High Demand</option><option>Available</option><option>Low Demand</option></select>
      </div>
      <div id="asset-table"></div>
    </div>`;
  renderAssetTable();
}
function renderAssetTable(){
  const fr=document.getElementById('af-reg')?.value||'',fc=document.getElementById('af-cls')?.value||'',fs=document.getElementById('af-st')?.value||'';
  const fl=state.assets.filter(a=>(!fr||a.region===fr)&&(!fc||a.assetClass===fc)&&(!fs||a.status===fs));
  const el=document.getElementById('asset-table');if(!el)return;
  const sm={'High Demand':'Approved','Available':'Pending Approval','Low Demand':'Rejected'};
  el.innerHTML=fl.length===0?emptyState('No assets match','Adjust filters.'):`<div class="table-wrap"><table><thead><tr><th>Code</th><th>Class</th><th>Region</th><th>Traffic</th><th>Audience</th><th>Occupancy</th><th>Size</th><th>Status</th></tr></thead><tbody>
    ${fl.map(a=>`<tr><td class="mono" style="font-weight:700;">${a.code}</td><td>${a.assetClass}</td><td>${a.region}</td><td class="mono">${a.trafficVolume.toLocaleString()}</td><td class="mono">${a.audienceReach.toLocaleString()}</td><td><div style="display:flex;align-items:center;gap:8px;"><span class="mono" style="font-weight:600;">${a.occupancy}%</span><div style="width:60px;">${progressBar(a.occupancy,a.occupancy>=60?'var(--green)':a.occupancy>=40?'var(--amber)':'var(--red)')}</div></div></td><td class="mono">${a.sizeSqm}</td><td>${statusChip(sm[a.status]||'Pending Approval')}</td></tr>`).join('')}
  </tbody></table></div>`;
}
function openAssetForm(){
  const slot=document.getElementById('af-slot');
  slot.innerHTML=`<div class="card" style="margin-bottom:16px;border-color:var(--accent);"><div class="section-title">Add New Asset</div>
    <div class="form-row triple"><div><label>Asset Code</label><input id="na-code" placeholder="e.g. DB-NM-099"></div><div><label>Class</label><select id="na-cls">${[...new Set(state.assets.map(a=>a.assetClass))].map(c=>`<option>${c}</option>`).join('')}</select></div><div><label>Region</label><select id="na-reg">${[...new Set(state.assets.map(a=>a.region))].map(r=>`<option>${r}</option>`).join('')}</select></div></div>
    <div class="form-row triple"><div><label>Traffic Volume</label><input id="na-tr" type="number" placeholder="e.g. 75000"></div><div><label>Occupancy %</label><input id="na-oc" type="number" placeholder="0-100" min="0" max="100"></div><div><label>Size (sqm)</label><input id="na-sz" type="number" placeholder="e.g. 2.1" step="0.1"></div></div>
    <div style="display:flex;gap:8px;"><button class="btn btn-dark" onclick="submitAsset()">Save Asset</button><button class="btn" onclick="document.getElementById('af-slot').innerHTML=''">Cancel</button></div>
  </div>`;
}
function submitAsset(){
  const code=document.getElementById('na-code').value.trim(),traffic=parseFloat(document.getElementById('na-tr').value)||0;
  if(!code||!traffic){showToast('Code and traffic required','error');return;}
  const occ=parseFloat(document.getElementById('na-oc').value)||0;
  const a={id:'AST-'+String(state.assets.length+1).padStart(3,'0'),code,region:document.getElementById('na-reg').value,assetClass:document.getElementById('na-cls').value,trafficVolume:traffic,audienceReach:Math.round(traffic*0.62),occupancy:occ,sizeSqm:parseFloat(document.getElementById('na-sz').value)||1.0,status:occ>60?'High Demand':occ>40?'Available':'Low Demand',lastUpdated:new Date().toISOString().slice(0,10)};
  state.assets.push(a);lsSet('pirop_a',state.assets);
  logAudit('Asset Added','Asset Catalogue',a.code+' — '+a.assetClass+' in '+a.region);
  document.getElementById('af-slot').innerHTML='';renderAssets(document.getElementById('main'));showToast(a.code+' added','success');
}

/* ---- PRICING WORKSPACE ---- */
let pricingDraft=null;
function renderPricing(m){
  m.innerHTML=`
    <div class="topbar"><div class="topbar-left"><h2>Pricing Workspace</h2><p>Benchmark-first pricing with explainable fallback recommendations — end-to-end asset selection to approval</p></div><div class="topbar-actions"><span class="chip chip-blue">${state.requests.length} Requests</span></div></div>
    <div class="grid grid-2">
      <div class="card">
        <div class="section-title">1 &middot; Select Asset &amp; Campaign</div>
        <div class="form-row full"><div><label>Asset</label><select id="pw-asset" onchange="previewAsset()">${state.assets.map(a=>`<option value="${a.id}">${a.code} — ${a.assetClass}, ${a.region}</option>`).join('')}</select></div></div>
        <div id="pw-preview" style="margin-bottom:14px;"></div>
        <div class="form-row"><div><label>Duration (days)</label><input id="pw-dur" type="number" value="30" min="1"></div><div><label>Customer</label><input id="pw-cust" type="text" placeholder="e.g. Nova Beverages"></div></div>
        <div class="form-row full"><div><label>Campaign Brief (optional)</label><textarea id="pw-brief" placeholder="Campaign objectives..."></textarea></div></div>
        <button class="btn btn-dark" style="width:100%;" onclick="runRecommendation()">Run Pricing Recommendation</button>
      </div>
      <div class="card" id="pw-result">${emptyState('No recommendation yet','Select an asset and run the pricing engine.')}</div>
    </div>
    <div class="card" style="margin-top:16px;" id="pw-submit"></div>
    <div class="card" style="margin-top:16px;"><div class="section-title">My Recent Requests</div>${state.requests.filter(r=>r.createdBy===state.user).length===0?'<p style="color:var(--text-dim);font-size:13px;">No requests submitted yet.</p>':reqTable(state.requests.filter(r=>r.createdBy===state.user).slice(0,5))}</div>`;
  previewAsset();
}
function previewAsset(){
  const id=document.getElementById('pw-asset')?.value,a=state.assets.find(x=>x.id===id);
  const el=document.getElementById('pw-preview');if(!el||!a)return;
  const bms=matchBMs(a).length;
  el.innerHTML=`<div style="background:var(--paper);border-radius:8px;padding:12px;font-size:12.5px;display:grid;grid-template-columns:1fr 1fr;gap:8px;">
    <div><span style="color:var(--text-dim);">Traffic</span><br><strong>${a.trafficVolume.toLocaleString()}</strong></div>
    <div><span style="color:var(--text-dim);">Audience Reach</span><br><strong>${a.audienceReach.toLocaleString()}</strong></div>
    <div><span style="color:var(--text-dim);">Occupancy</span><br><strong style="color:${a.occupancy>=65?'var(--green)':a.occupancy>=40?'var(--amber)':'var(--red)'};">${a.occupancy}% — ${a.status}</strong></div>
    <div><span style="color:var(--text-dim);">PPU Benchmarks</span><br><strong style="color:${bms>0?'var(--green)':'var(--amber)'};">${bms>0?bms+' found':'None — Fallback applies'}</strong></div>
  </div>`;
}
function runRecommendation(){
  const id=document.getElementById('pw-asset').value,dur=parseInt(document.getElementById('pw-dur').value)||30,cust=document.getElementById('pw-cust').value.trim()||'Unnamed Prospect';
  const a=state.assets.find(x=>x.id===id);if(!a){showToast('Select a valid asset','error');return;}
  const res=runPricingEngine(a,dur);pricingDraft={asset:a,duration:dur,customer:cust,...res};
  document.getElementById('pw-result').innerHTML=`
    <div class="section-title">2 &middot; Recommendation &mdash; ${res.method}</div>
    <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:4px;"><div class="mono" style="font-size:28px;font-weight:700;">&#8377;${res.suggestedPrice.toLocaleString('en-IN')}</div><span class="chip ${res.method==='Benchmark Match'?'chip-blue':'chip-amber'}">${res.method}</span></div>
    <div style="font-size:12px;color:var(--text-dim);margin-bottom:12px;">&#8377;${res.dailyRate.toLocaleString('en-IN')}/day &times; ${dur} days</div>
    ${confidenceMeter(res.confidence)}
    <div class="constellation">${constellationSVG(a.code,res.comparables)}</div>
    <div class="rationale-box"><b>Rationale:</b> ${res.rationale}</div>`;
  document.getElementById('pw-submit').innerHTML=`
    <div class="section-title">3 &middot; Finalize &amp; Submit</div>
    <div class="form-row"><div><label>Final Price (&#8377;)</label><input id="pw-fp" type="number" value="${res.suggestedPrice}"></div><div><label>Analyst Notes</label><input id="pw-notes" type="text" placeholder="Override justification..."></div></div>
    <button class="btn btn-dark" onclick="submitPricingReq()">Submit for Approval &#8594;</button>`;
  document.getElementById('pw-submit').scrollIntoView({behavior:'smooth',block:'start'});
}
function submitPricingReq(){
  if(!pricingDraft)return;
  const fp=parseFloat(document.getElementById('pw-fp').value)||pricingDraft.suggestedPrice;
  const notes=document.getElementById('pw-notes').value;
  const req={id:'PR-'+String(state.requests.length+1001),assetId:pricingDraft.asset.id,customer:pricingDraft.customer,duration:pricingDraft.duration,method:pricingDraft.method,confidence:pricingDraft.confidence,suggestedPrice:pricingDraft.suggestedPrice,finalPrice:fp,notes,status:'Pending Approval',createdBy:state.user,createdAt:new Date().toISOString(),rationale:pricingDraft.rationale,decidedBy:null,decidedAt:null,decisionComment:''};
  state.requests.unshift(req);saveReqs();
  logAudit('Pricing Request Submitted','Pricing',req.id+' for '+pricingDraft.asset.code+' @ INR '+fp.toLocaleString('en-IN')+' ('+req.method+', '+req.confidence+'% conf)'+(notes?' — '+notes:''));
  pricingDraft=null;showToast(req.id+' submitted','success');renderPricing(document.getElementById('main'));
}

/* ---- SCENARIO PLANNING ---- */
let selScenario=null;
function renderScenario(m){
  const approved=state.requests.filter(r=>r.status==='Approved');
  const baseRev=approved.reduce((s,r)=>s+(r.finalPrice||0),0)||4500000;
  const avgOcc=state.assets.length?Math.round(state.assets.reduce((s,a)=>s+a.occupancy,0)/state.assets.length):55;
  m.innerHTML=`
    <div class="topbar"><div class="topbar-left"><h2>Scenario Planning</h2><p>Model commercial outcomes across pricing strategies — compare base case, growth, and premium positioning</p></div><div class="topbar-actions"><button class="btn btn-dark" onclick="openScenarioForm()">+ New Scenario</button></div></div>
    <div id="scn-slot"></div>
    <div class="grid grid-3" style="margin-bottom:18px;">
      ${state.scenarios.map(s=>{const adjRev=Math.round(baseRev*(1+s.priceAdjustment/100));const delta=adjRev-baseRev;return `<div class="scenario-card ${selScenario&&selScenario.id===s.id?'selected':''}" onclick="selectScenario('${s.id}')">
        <div style="font-size:11px;color:var(--text-dim);font-weight:700;text-transform:uppercase;margin-bottom:4px;">${s.id}</div>
        <div style="font-weight:700;font-size:15px;margin-bottom:4px;">${s.name}</div>
        <div style="font-size:12px;color:var(--text-dim);margin-bottom:12px;">${s.description}</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:10px;"><div><div class="mono" style="font-size:18px;font-weight:600;">&#8377;${Math.round(adjRev/1000)}k</div><div style="font-size:11.5px;color:var(--text-dim);">Proj. Revenue</div></div><div><div class="mono" style="font-size:18px;font-weight:600;">${s.occupancyTarget}%</div><div style="font-size:11.5px;color:var(--text-dim);">Target Occ.</div></div></div>
        <div style="font-size:12px;font-weight:600;color:${delta>=0?'var(--green)':'var(--red)'};">${delta>=0?'&uarr;':'&darr;'} &#8377;${Math.abs(delta).toLocaleString('en-IN')} vs base</div>
        <div style="font-size:11.5px;color:var(--text-dim);margin-top:4px;">Price adj: ${s.priceAdjustment>=0?'+':''}${s.priceAdjustment}% &middot; Discount cap: ${s.discountCap}%</div>
      </div>`;}).join('')}
    </div>
    <div class="card" style="margin-bottom:16px;"><div class="section-title">Scenario Comparison</div><canvas id="cScn" height="200"></canvas></div>
    <div class="card" id="scn-detail">${emptyState('Select a scenario to view details','Choose one of the scenario models above.')}</div>`;
  const scnL=state.scenarios.map(s=>s.name);
  createSafeChart('cScn',{type:'bar',data:{labels:scnL,datasets:[{label:'Projected Revenue',data:state.scenarios.map(s=>Math.round(baseRev*(1+s.priceAdjustment/100))),backgroundColor:['#2F5EFF','#0F8A55','#7C3AED'],borderRadius:6,yAxisID:'y'},{label:'Target Occ. %',data:state.scenarios.map(s=>s.occupancyTarget),backgroundColor:['rgba(47,94,255,.2)','rgba(15,138,85,.2)','rgba(124,58,237,.2)'],borderRadius:4,yAxisID:'y1'}]},options:{plugins:{legend:{position:'bottom',labels:{boxWidth:10}}},scales:{y:{position:'left',grid:{color:'#EEF0F5'},ticks:{callback:v=>'INR'+Math.round(v/1000)+'k'}},y1:{position:'right',max:100,grid:{drawOnChartArea:false},ticks:{callback:v=>v+'%'}}}}});
  if(selScenario)selectScenario(selScenario.id);
}
function selectScenario(id){
  selScenario=state.scenarios.find(s=>s.id===id);if(!selScenario)return;
  const approved=state.requests.filter(r=>r.status==='Approved');
  const baseRev=approved.reduce((s,r)=>s+(r.finalPrice||0),0)||4500000;
  const adjRev=Math.round(baseRev*(1+selScenario.priceAdjustment/100));
  const delta=adjRev-baseRev;
  const avgOcc=state.assets.length?Math.round(state.assets.reduce((s,a)=>s+a.occupancy,0)/state.assets.length):55;
  const panel=document.getElementById('scn-detail');if(!panel)return;
  panel.innerHTML=`
    <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
      <div><div class="section-title" style="margin-bottom:4px;">Scenario Detail</div><h3>${selScenario.name}</h3><p style="color:var(--text-dim);font-size:13px;margin-top:4px;">${selScenario.description}</p></div>
      <div style="text-align:right;"><div class="mono" style="font-size:22px;font-weight:700;">&#8377;${adjRev.toLocaleString('en-IN')}</div><div style="font-size:12px;font-weight:600;color:${delta>=0?'var(--green)':'var(--red)'};">${delta>=0?'+':''}&#8377;${Math.abs(delta).toLocaleString('en-IN')} vs base</div></div>
    </div>
    <div class="grid grid-3" style="margin-bottom:16px;">
      <div class="card kpi-card"><div class="kpi-label">Price Adjustment</div><div class="kpi-value" style="font-size:22px;color:${selScenario.priceAdjustment>=0?'var(--green)':'var(--red)'};">${selScenario.priceAdjustment>=0?'+':''}${selScenario.priceAdjustment}%</div></div>
      <div class="card kpi-card"><div class="kpi-label">Target Occupancy</div><div class="kpi-value" style="font-size:22px;">${selScenario.occupancyTarget}%</div><div class="kpi-delta">vs current ${avgOcc}%</div></div>
      <div class="card kpi-card"><div class="kpi-label">Max Discount Cap</div><div class="kpi-value" style="font-size:22px;">${selScenario.discountCap}%</div></div>
    </div>
    <div class="rationale-box">Applying a ${selScenario.priceAdjustment>=0?'price increase':'reduction'} of ${Math.abs(selScenario.priceAdjustment)}% projects revenue to <b>&#8377;${adjRev.toLocaleString('en-IN')}</b> with target occupancy <b>${selScenario.occupancyTarget}%</b>. Max discount: <b>${selScenario.discountCap}%</b> from list rate.</div>
    <div style="margin-top:14px;display:flex;gap:8px;">
      <button class="btn btn-dark" onclick="goTab('pricing')">Apply in Pricing Workspace &#8594;</button>
      ${state.role==='admin'?`<button class="btn btn-red btn-sm" onclick="deleteScenario('${selScenario.id}')">Delete</button>`:''}
    </div>`;
  document.querySelectorAll('.scenario-card').forEach(el=>el.classList.toggle('selected',el.getAttribute('onclick').includes("'"+id+"'")));
}
function openScenarioForm(){
  const slot=document.getElementById('scn-slot');
  slot.innerHTML=`<div class="card" style="margin-bottom:16px;border-color:var(--accent);"><div class="section-title">New Scenario</div>
    <div class="form-row"><div><label>Name</label><input id="sn-name" placeholder="e.g. Q4 Festival Push"></div><div><label>Description</label><input id="sn-desc" placeholder="Brief description"></div></div>
    <div class="form-row triple"><div><label>Price Adj. (%)</label><input id="sn-price" type="number" value="0" placeholder="+15 or -10"></div><div><label>Target Occ. (%)</label><input id="sn-occ" type="number" value="60" min="0" max="100"></div><div><label>Discount Cap (%)</label><input id="sn-disc" type="number" value="10" min="0" max="50"></div></div>
    <div style="display:flex;gap:8px;"><button class="btn btn-dark" onclick="saveScenario()">Save Scenario</button><button class="btn" onclick="document.getElementById('scn-slot').innerHTML=''">Cancel</button></div>
  </div>`;
}
function saveScenario(){
  const name=document.getElementById('sn-name').value.trim();if(!name){showToast('Name required','error');return;}
  const s={id:'SCN-'+String(state.scenarios.length+1).padStart(3,'0'),name,description:document.getElementById('sn-desc').value||'',priceAdjustment:parseFloat(document.getElementById('sn-price').value)||0,occupancyTarget:parseFloat(document.getElementById('sn-occ').value)||60,discountCap:parseFloat(document.getElementById('sn-disc').value)||10,createdAt:new Date().toISOString()};
  state.scenarios.push(s);saveScen();
  logAudit('Scenario Created','Scenario Planning',s.id+' "'+s.name+'" ('+s.priceAdjustment+'% price, '+s.occupancyTarget+'% occ target)');
  document.getElementById('scn-slot').innerHTML='';renderScenario(document.getElementById('main'));showToast('"'+s.name+'" created','success');
}
function deleteScenario(id){
  if(!confirm('Delete this scenario?'))return;
  state.scenarios=state.scenarios.filter(s=>s.id!==id);saveScen();selScenario=null;
  renderScenario(document.getElementById('main'));showToast('Scenario deleted','info');
}

/* ---- FINANCIAL FEASIBILITY ---- */
let lastFin=null;
function renderFinanceModule(m){
  m.innerHTML=`
    <div class="topbar"><div class="topbar-left"><h2>Financial Feasibility Engine</h2><p>ROI, IRR, NPV, payback period &amp; MAG modelling for commercial deals</p></div></div>
    <div class="grid grid-2" style="margin-bottom:18px;">
      <div class="card">
        <div class="section-title">Model Inputs</div>
        <div class="form-row"><div><label>Total Revenue (&#8377;)</label><input id="ff-rev" type="number" value="4500000" step="100000"></div><div><label>Total Cost (&#8377;)</label><input id="ff-cost" type="number" value="2800000" step="100000"></div></div>
        <div class="form-row"><div><label>Term (Years)</label><input id="ff-yrs" type="number" value="3" min="1" max="10"></div><div><label>Discount Rate (%)</label><input id="ff-dr" type="number" value="12" step="0.5"></div></div>
        <div class="form-row"><div><label>Revenue Share (%)</label><input id="ff-rs" type="number" value="18" step="0.5"></div><div><label>MAG per Year (&#8377;)</label><input id="ff-mag" type="number" value="900000" step="50000"></div></div>
        <button class="btn btn-dark" style="width:100%;" onclick="runFeasibility()">Calculate Feasibility</button>
        <div style="margin-top:10px;font-size:12px;color:var(--text-dim);">Results: ROI &middot; IRR (bisection) &middot; NPV &middot; Payback &middot; MAG vs. revenue share</div>
      </div>
      <div class="card" id="ff-result">${emptyState('No model run yet','Enter assumptions and calculate.')}</div>
    </div>
    <div class="card" id="ff-chart" style="display:none;margin-bottom:16px;"><div class="section-title">Cash Flow Projection</div><canvas id="cCF" height="160"></canvas></div>
    <div class="card" id="ff-hist">
      <div class="section-title">Saved Models</div>
      ${state.financialModels.length===0?'<p style="color:var(--text-dim);font-size:13px;">No saved models yet.</p>':`<div class="table-wrap"><table><thead><tr><th>ID</th><th>Revenue</th><th>Cost</th><th>Term</th><th>ROI</th><th>NPV</th><th>IRR</th><th>Saved</th></tr></thead><tbody>${state.financialModels.slice(0,8).map(f=>`<tr><td class="mono">${f.id}</td><td class="mono">&#8377;${f.revenueTotal.toLocaleString('en-IN')}</td><td class="mono">&#8377;${f.costTotal.toLocaleString('en-IN')}</td><td>${f.years}yr</td><td style="font-weight:700;color:${f.roi>=20?'var(--green)':f.roi>=0?'var(--amber)':'var(--red)'};">${f.roi.toFixed(1)}%</td><td class="mono">&#8377;${Math.round(f.npv).toLocaleString('en-IN')}</td><td>${f.irr.toFixed(1)}%</td><td class="mono" style="font-size:11px;color:var(--text-dim);">${new Date(f.savedAt).toLocaleDateString('en-IN')}</td></tr>`).join('')}</tbody></table></div>`}
    </div>`;
}
function runFeasibility(){
  const revenueTotal=parseFloat(document.getElementById('ff-rev').value)||0,costTotal=parseFloat(document.getElementById('ff-cost').value)||0;
  const years=parseInt(document.getElementById('ff-yrs').value)||1,discountRate=parseFloat(document.getElementById('ff-dr').value)||0;
  const revenueSharePct=parseFloat(document.getElementById('ff-rs').value)||0,mag=parseFloat(document.getElementById('ff-mag').value)||0;
  if(!revenueTotal||!costTotal){showToast('Enter revenue and cost','error');return;}
  const r=financialFeasibility({revenueTotal,costTotal,years,discountRate,revenueSharePct,mag});
  lastFin={revenueTotal,costTotal,years,discountRate,revenueSharePct,mag,...r};
  const rc=r.roi>=20?'var(--green)':r.roi>=0?'var(--amber)':'var(--red)',nc=r.npv>=0?'var(--green)':'var(--red)';
  document.getElementById('ff-result').innerHTML=`
    <div class="section-title">Results</div>
    <div class="grid grid-2" style="margin-bottom:14px;">
      <div class="card kpi-card"><div class="kpi-label">ROI</div><div class="kpi-value" style="color:${rc};">${r.roi.toFixed(1)}%</div></div>
      <div class="card kpi-card"><div class="kpi-label">NPV</div><div class="kpi-value" style="font-size:20px;color:${nc};">&#8377;${Math.round(r.npv).toLocaleString('en-IN')}</div><div class="kpi-delta">at ${discountRate}% rate</div></div>
      <div class="card kpi-card"><div class="kpi-label">IRR</div><div class="kpi-value">${isFinite(r.irr)?r.irr.toFixed(1)+'%':'n/a'}</div></div>
      <div class="card kpi-card"><div class="kpi-label">Payback</div><div class="kpi-value" style="font-size:20px;">${r.payback?r.payback.toFixed(1)+' yrs':'> term'}</div></div>
      <div class="card kpi-card"><div class="kpi-label">Annual Revenue</div><div class="kpi-value" style="font-size:20px;">&#8377;${Math.round(r.annualRevenue).toLocaleString('en-IN')}</div></div>
      <div class="card kpi-card"><div class="kpi-label">Breakeven Occ.</div><div class="kpi-value" style="font-size:20px;">${r.breakevenOcc}%</div></div>
    </div>
    <div class="rationale-box">Revenue share of ${revenueSharePct}% yields <b>&#8377;${Math.round(r.revenueShareAmt).toLocaleString('en-IN')}</b> vs. MAG floor <b>&#8377;${(mag*years).toLocaleString('en-IN')}</b>. Guarantee: <b>&#8377;${Math.round(r.guaranteedTake).toLocaleString('en-IN')}</b> (${r.guaranteedTake===mag*years?'MAG governs':'revenue share governs'}). ${r.npv>=0?'Deal creates positive value at stated discount rate.':'<b>Caution:</b> Negative NPV — review deal economics.'}</div>
    <div style="margin-top:12px;display:flex;gap:8px;"><button class="btn btn-dark btn-sm" onclick="saveFinModel()">Save Model</button><button class="btn btn-sm" onclick="renderFinanceModule(document.getElementById('main'))">Reset</button></div>`;
  const fc=document.getElementById('ff-chart');fc.style.display='block';fc.style.marginTop='16px';
  const cum=[];let running=-costTotal;r.cashFlows.forEach(cf=>{running+=cf;cum.push(Math.round(running));});
  createSafeChart('cCF',{type:'bar',data:{labels:Array.from({length:years},(_,i)=>'Year '+(i+1)),datasets:[{label:'Cash Flow',data:r.cashFlows.map(Math.round),backgroundColor:'#2F5EFF',borderRadius:5},{label:'Cumulative',data:cum,type:'line',borderColor:'#0F8A55',backgroundColor:'rgba(15,138,85,.08)',tension:.3,fill:true,yAxisID:'y'}]},options:{plugins:{legend:{position:'bottom',labels:{boxWidth:10}}},scales:{y:{grid:{color:'#EEF0F5'},ticks:{callback:v=>'INR'+Math.round(v/1000)+'k'}}}}});
}
function saveFinModel(){
  if(!lastFin){showToast('Run a calculation first','error');return;}
  const fm={id:'FIN-'+String(state.financialModels.length+1).padStart(3,'0'),...lastFin,savedAt:new Date().toISOString(),savedBy:state.user};
  state.financialModels.unshift(fm);saveFin();
  logAudit('Financial Model Saved','Financial Feasibility',fm.id+' — ROI '+fm.roi.toFixed(1)+'%, NPV INR '+Math.round(fm.npv).toLocaleString('en-IN')+', IRR '+fm.irr.toFixed(1)+'%');
  renderFinanceModule(document.getElementById('main'));showToast(fm.id+' saved','success');
}

/* ---- APPROVALS ---- */
function renderApprovals(m){
  const pending=state.requests.filter(r=>r.status==='Pending Approval');
  const decided=state.requests.filter(r=>r.status==='Approved'||r.status==='Rejected');
  m.innerHTML=`
    <div class="topbar"><div class="topbar-left"><h2>Approvals Queue</h2><p>Commercial governance — review, approve or reject pending pricing decisions with full rationale</p></div><div class="topbar-actions"><span class="chip ${pending.length>0?'chip-amber':'chip-green'}">${pending.length} awaiting review</span></div></div>
    ${pending.length===0?`<div class="card">${emptyState('Queue is clear','No pricing requests pending approval.')}</div>`:
    pending.map(r=>{
      const a=state.assets.find(x=>x.id===r.assetId);const isHR=r.method==='Intelligent Fallback'||r.confidence<65;
      return `<div class="card" style="margin-bottom:14px;${isHR?'border-color:var(--amber);':''}">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;">
          <div><div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;"><b class="mono" style="font-size:15px;">${r.id}</b>${isHR?'<span class="chip chip-amber">Review Required</span>':''}</div>
            <div style="font-size:14px;font-weight:600;">${a?a.code:'—'} &mdash; ${a?a.assetClass:''}, ${a?a.region:''}</div>
            <div style="color:var(--text-dim);font-size:12.5px;margin-top:2px;">Customer: <b>${r.customer}</b> &middot; ${r.duration} days &middot; by ${r.createdBy} &middot; ${new Date(r.createdAt).toLocaleDateString('en-IN')}</div>
          </div>
          <div style="text-align:right;flex-shrink:0;">
            <div class="mono" style="font-size:22px;font-weight:700;">&#8377;${(r.finalPrice||r.suggestedPrice||0).toLocaleString('en-IN')}</div>
            <div style="font-size:12px;color:var(--text-dim);">&#8377;${Math.round((r.finalPrice||r.suggestedPrice||0)/r.duration).toLocaleString('en-IN')}/day</div>
            <div style="margin-top:4px;"><span class="chip ${r.method==='Benchmark Match'?'chip-blue':'chip-amber'}">${r.method}</span> <span style="font-weight:700;color:${r.confidence>=75?'var(--green)':r.confidence>=50?'var(--amber)':'var(--red)'};">${r.confidence}%</span></div>
          </div>
        </div>
        ${confidenceMeter(r.confidence)}
        <div class="rationale-box">${r.rationale}${r.notes?'<br><br><b>Analyst note:</b> '+r.notes:''}</div>
        <div style="display:flex;gap:8px;margin-top:14px;">
          <button class="btn btn-green" onclick="decideReq('${r.id}','Approved')">&#10003; Approve</button>
          <button class="btn btn-red" onclick="decideReq('${r.id}','Rejected')">&#10007; Reject</button>
          <button class="btn btn-sm" onclick="viewAsset('${r.assetId}')">View Asset</button>
        </div>
      </div>`;
    }).join('')}
    ${decided.length>0?`<div class="card" style="margin-top:8px;"><div class="section-title">Decision History</div>${reqTable(decided.slice(0,8))}</div>`:''}`;
}
function decideReq(id,decision){
  const req=state.requests.find(r=>r.id===id);if(!req)return;
  const comment=prompt((decision==='Approved'?'Approval':'Rejection')+' comment (optional):','');
  req.status=decision;req.decidedBy=state.user;req.decidedAt=new Date().toISOString();req.decisionComment=comment||'';
  saveReqs();logAudit(decision+' Pricing Request','Approval',req.id+' '+decision.toLowerCase()+' by '+state.user+(comment?' — "'+comment+'"':''));
  showToast(req.id+' '+decision.toLowerCase(),'success');renderApprovals(document.getElementById('main'));
}
function viewAsset(assetId){
  const a=state.assets.find(x=>x.id===assetId);if(!a)return;
  const ov=document.createElement('div');ov.className='modal-overlay';
  ov.innerHTML=`<div class="modal-box"><div class="modal-title">Asset &mdash; ${a.code}</div><div class="modal-sub">${a.assetClass} &middot; ${a.region}</div>
    <div class="grid grid-2">
      <div class="card kpi-card"><div class="kpi-label">Traffic Volume</div><div class="kpi-value" style="font-size:20px;">${a.trafficVolume.toLocaleString()}</div></div>
      <div class="card kpi-card"><div class="kpi-label">Audience Reach</div><div class="kpi-value" style="font-size:20px;">${a.audienceReach.toLocaleString()}</div></div>
      <div class="card kpi-card"><div class="kpi-label">Occupancy</div><div class="kpi-value" style="font-size:20px;">${a.occupancy}%</div></div>
      <div class="card kpi-card"><div class="kpi-label">Status</div><div class="kpi-value" style="font-size:18px;">${a.status}</div></div>
    </div>
    <div class="modal-footer"><button class="btn btn-dark" onclick="this.closest('.modal-overlay').remove()">Close</button></div>
  </div>`;
  document.body.appendChild(ov);ov.addEventListener('click',e=>{if(e.target===ov)ov.remove();});
}

/* ---- GOVERNANCE ---- */
function renderGovernance(m){
  m.innerHTML=`
    <div class="topbar"><div class="topbar-left"><h2>Governance &amp; Audit Trail</h2><p>Immutable append-only log of every pricing decision, benchmark change, and approval action</p></div><div class="topbar-actions"><button class="btn btn-sm" onclick="exportAudit()">&#8595; Export CSV</button></div></div>
    <div class="grid grid-4" style="margin-bottom:18px;">
      <div class="card kpi-card"><div class="kpi-label">Audit Events</div><div class="kpi-value">${state.audit.length}</div><div class="kpi-delta">total logged actions</div></div>
      <div class="card kpi-card"><div class="kpi-label">Pricing Requests</div><div class="kpi-value">${state.requests.length}</div><div class="kpi-delta">${state.requests.filter(r=>r.status==='Approved').length} approved</div></div>
      <div class="card kpi-card"><div class="kpi-label">Benchmarks</div><div class="kpi-value">${state.benchmarks.length}</div><div class="kpi-delta">PPU entries</div></div>
      <div class="card kpi-card"><div class="kpi-label">Active Users</div><div class="kpi-value">${[...new Set(state.audit.map(e=>e.actor.split(' (')[0]).filter(a=>a!=='System'))].length}</div><div class="kpi-delta">unique actors</div></div>
    </div>
    <div class="card" style="margin-bottom:16px;"><div class="section-title">Active Governance Policies</div>
      <div class="grid grid-3">${[
        ['01','Benchmark-First Pricing','All requests must attempt PPU benchmark match before applying Intelligent Fallback.'],
        ['02','Human-in-the-Loop Approval','Fallback pricing (confidence < 70%) requires commercial approver sign-off within 24 hours.'],
        ['03','Immutable Audit Log','Every mutation is logged — no deletions permitted on the audit trail.'],
        ['04','RBAC Access Control','Role-based access enforced: analysts cannot approve, approvers cannot modify benchmarks.'],
        ['05','Source Traceability','All PPU benchmarks must declare data source type (investor rate card, mystery shopping, contract).'],
        ['06','Confidence Disclosure','Confidence score must be visible to approvers for all pending pricing requests.'],
      ].map(([ic,t,d])=>`<div class="insight-card"><div class="insight-icon">${ic}</div><div class="insight-body"><h4>${t}</h4><p>${d}</p></div></div>`).join('')}
    </div></div>
    <div class="card"><div class="card-header"><div class="section-title" style="margin-bottom:0;">Activity Log</div><span style="font-size:12px;color:var(--text-dim);">${state.audit.length} events</span></div>
      <div style="max-height:480px;overflow-y:auto;">
        ${state.audit.map(e=>`<div class="audit-item"><b>${e.action}</b> <span style="color:var(--text-dim);font-size:12px;">&mdash; ${e.entity}</span><div style="margin-top:3px;">${e.details||''}</div><div class="audit-meta">Actor: ${e.actor} &middot; Time: ${new Date(e.ts).toLocaleString('en-IN')}</div></div>`).join('')}
      </div>
    </div>`;
}
function exportAudit(){
  const rows=[['ID','Timestamp','Actor','Action','Entity','Details']];
  state.audit.forEach(e=>rows.push([e.id,e.ts,e.actor,e.action,e.entity,(e.details||'').replace(/,/g,';')]));
  const csv=rows.map(r=>r.map(v=>`"${v}"`).join(',')).join('\n');
  const a=document.createElement('a');a.href='data:text/csv;charset=utf-8,'+encodeURIComponent(csv);a.download='PIROP_Audit_'+new Date().toISOString().slice(0,10)+'.csv';a.click();
  showToast('Audit log exported','success');
}

/* ---- COMMERCIAL INTELLIGENCE ---- */
let copilotHistory=[];
function renderCopilot(m){
  m.innerHTML=`
    <div class="topbar"><div class="topbar-left"><h2>Commercial Intelligence</h2><p>Ask natural-language questions about pricing, occupancy, and portfolio strategy &mdash; grounded in live data</p></div><div class="topbar-actions"><span class="chip chip-purple">Commercial Engine</span>${copilotHistory.length>0?'<button class="btn btn-sm" onclick="clearCopilot()">Clear</button>':''}</div></div>
    <div class="copilot-wrap">
      <div class="copilot-log" id="cop-log">
        ${copilotHistory.length===0?`<div style="padding:10px 0 16px;"><div style="font-size:13px;color:var(--text-dim);margin-bottom:12px;"><strong>Suggested questions:</strong></div><div class="suggestion-chips">
          <span class="suggestion-chip" onclick="askCopilot('What is our average selling price and win rate?')">Selling price &amp; win rate?</span>
          <span class="suggestion-chip" onclick="askCopilot('Which region has the highest occupancy?')">Highest occupancy region?</span>
          <span class="suggestion-chip" onclick="askCopilot('Explain benchmark match vs fallback pricing.')">Benchmark vs fallback?</span>
          <span class="suggestion-chip" onclick="askCopilot('Which assets are underperforming and what should we do?')">Underperforming assets?</span>
          <span class="suggestion-chip" onclick="askCopilot('How many pricing requests are pending approval?')">Pending approvals?</span>
          <span class="suggestion-chip" onclick="askCopilot('What PPU coverage gaps exist and which assets are affected?')">PPU coverage gaps?</span>
          <span class="suggestion-chip" onclick="askCopilot('Give me a revenue optimization plan for next quarter.')">Revenue optimization plan?</span>
          <span class="suggestion-chip" onclick="askCopilot('Summarize the full portfolio performance.')">Portfolio summary?</span>
        </div></div>`:copilotHistory.map(h=>`<div class="msg ${h.role==='user'?'msg-user':'msg-ai'}">${h.text}</div>`).join('')}
      </div>
      <div class="copilot-input">
        <input id="cop-box" type="text" placeholder="Ask about pricing, revenue, occupancy, or strategy..." onkeydown="if(event.key==='Enter')askCopilot()">
        <button class="btn btn-dark" onclick="askCopilot()">Ask &#8594;</button>
      </div>
    </div>`;
  setTimeout(()=>{const l=document.getElementById('cop-log');if(l)l.scrollTop=l.scrollHeight;},50);
}
function clearCopilot(){copilotHistory=[];renderCopilot(document.getElementById('main'));}

function generateCopilotResponse(q){
  const ql=q.toLowerCase();
  const reqs=state.requests,approved=reqs.filter(r=>r.status==='Approved'),pending=reqs.filter(r=>r.status==='Pending Approval');
  const totalRev=approved.reduce((s,r)=>s+(r.finalPrice||0),0);
  const avgOcc=state.assets.length?Math.round(state.assets.reduce((s,a)=>s+a.occupancy,0)/state.assets.length):0;
  const winRate=reqs.length?Math.round(100*approved.length/reqs.length):0;
  const asp=approved.length?Math.round(totalRev/approved.length):0;
  const hi=state.assets.filter(a=>a.occupancy>=65),lo=state.assets.filter(a=>a.occupancy<40);
  const fb=reqs.filter(r=>r.method==='Intelligent Fallback');
  const uncov=state.assets.filter(a=>matchBMs(a).length===0);

  if(ql.includes('win rate')||ql.includes('selling price')||ql.includes('asp')){
    return `Portfolio Commercial Summary\n\nWin rate: ${winRate}% across ${reqs.length} total requests.\nApproved: ${approved.length} | Pending: ${pending.length} | Rejected: ${reqs.filter(r=>r.status==='Rejected').length}\n\nAvg Selling Price: INR ${asp.toLocaleString('en-IN')} per deal.\nTotal realized revenue: INR ${totalRev.toLocaleString('en-IN')}\n\n${winRate>=60?'Win rate is healthy (above 60% benchmark).':'Win rate below 60% — review rejection patterns and pricing calibration.'}`;
  }
  if((ql.includes('highest')||ql.includes('best')||ql.includes('top'))&&ql.includes('occupancy')){
    const sorted=[...state.assets].sort((a,b)=>b.occupancy-a.occupancy);
    return `Highest Occupancy Assets\n\nTop 3:\n${sorted.slice(0,3).map((a,i)=>`${i+1}. ${a.code} (${a.assetClass}, ${a.region}) — ${a.occupancy}%`).join('\n')}\n\nPortfolio average: ${avgOcc}% vs. 55% target.\n${hi.length} asset${hi.length!==1?'s':''} above 65% — pricing headroom exists for a 12–18% rate uplift.`;
  }
  if(ql.includes('underperform')||ql.includes('low demand')||(ql.includes('low')&&ql.includes('occupancy'))){
    return lo.length===0?'All assets above 40% occupancy — portfolio health is positive. No underperforming assets currently.':
    `Underperforming Assets\n\n${lo.length} asset${lo.length!==1?'s':''} below 40% occupancy:\n${lo.map(a=>`- ${a.code} — ${a.region}, ${a.occupancy}%`).join('\n')}\n\nRecommendation: Consider 10–15% rate reduction or promotional bundling with high-demand assets in the same region to stimulate demand.`;
  }
  if(ql.includes('pending')||ql.includes('approval queue')||ql.includes('awaiting')){
    return pending.length===0?'Approvals Queue is clear — no pricing requests awaiting commercial approval.':
    `Pending Approvals — ${pending.length} request${pending.length!==1?'s':''}\n\n${pending.map(r=>{const a=state.assets.find(x=>x.id===r.assetId);return `- ${r.id} — ${a?a.code:'?'} (${r.customer}) | INR ${(r.finalPrice||r.suggestedPrice||0).toLocaleString('en-IN')} | ${r.method} | ${r.confidence}% conf`;}).join('\n')}\n\n${pending.filter(r=>r.method==='Intelligent Fallback').length>0?pending.filter(r=>r.method==='Intelligent Fallback').length+' fallback-priced request(s) require priority review per governance policy.':''}`;
  }
  if(ql.includes('explain')||ql.includes('difference')||(ql.includes('benchmark')&&ql.includes('fallback'))){
    return `Benchmark Match vs. Intelligent Fallback\n\nBenchmark Match (confidence 70–96%)\nUsed when the Price Point Universe has a matching rate record by asset class and region. Derived from average of matched records: investor rate cards, mystery shopping, or approved contracts. Higher confidence, lower risk.\n\nIntelligent Fallback (confidence 40–70%)\nApplied when no PPU benchmark exists. Engine evaluates traffic volume, audience reach, and occupancy, then cross-references 3 most similar assets by similarity score. Lower confidence — requires human review before approval per governance policy.\n\nCurrent status: ${state.benchmarks.length} PPU records active | ${fb.length} request(s) used fallback engine.`;
  }
  if(ql.includes('gap')||ql.includes('coverage')||(ql.includes('ppu')&&!ql.includes('explain'))){
    return `PPU Coverage Analysis\n\n${state.benchmarks.length} benchmark records across ${[...new Set(state.benchmarks.map(b=>b.assetClass+'/'+b.region))].length} class/region combinations.\n\n${uncov.length>0?'Coverage gaps ('+uncov.length+' assets without benchmark):\n'+uncov.map(a=>`- ${a.code} — ${a.assetClass} in ${a.region}`).join('\n')+'\n\nAdding PPU records for these assets would raise confidence scores and remove fallback dependency.':'Full PPU coverage — all assets have at least one benchmark record.'}`;
  }
  if(ql.includes('optim')||ql.includes('recommend')||ql.includes('strategy')||ql.includes('quarter')||ql.includes('plan')){
    return `Revenue Optimization Plan\n\n1. Rate Uplift on High-Demand Assets (High Priority)\n${hi.length} assets above 65% occupancy: ${hi.map(a=>a.code).join(', ')}.\nApply 12–18% rate increase — low demand elasticity at high occupancy.\n\n2. Fill Underperforming Inventory (Medium Priority)\n${lo.length>0?lo.map(a=>a.code).join(', ')+' at <40% occupancy.\nLaunch promotional bundles or cross-asset packages.':'All assets above 40% — continue monthly monitoring.'}\n\n3. Expand PPU Coverage (High Priority)\n${uncov.length} assets lack PPU benchmarks.\nCommission mystery shopping or collect historical contracts to shift these to Benchmark Match pricing.\n\n4. Clear Approvals Queue\n${pending.length} requests pending. Governance SLA: decide within 24 hours for fallback-priced requests.\n\nProjected impact: +8–15% revenue uplift if all recommendations are executed.`;
  }
  if(ql.includes('region')){
    const byR={};state.assets.forEach(a=>{if(!byR[a.region])byR[a.region]={assets:0,totalOcc:0};byR[a.region].assets++;byR[a.region].totalOcc+=a.occupancy;});
    return `Portfolio by Region\n\n${Object.entries(byR).map(([r,d])=>`${r}: ${d.assets} asset${d.assets!==1?'s':''} | Avg occ: ${Math.round(d.totalOcc/d.assets)}%`).join('\n')}\n\nBest performing region: ${Object.entries(byR).sort((a,b)=>(b[1].totalOcc/b[1].assets)-(a[1].totalOcc/a[1].assets))[0][0]}.`;
  }
  // Default summary
  return `PIROP Portfolio Snapshot — ${new Date().toLocaleDateString('en-IN',{month:'long',year:'numeric'})}\n\nCommercial:\n- Approved revenue: INR ${totalRev.toLocaleString('en-IN')} (${approved.length} deals)\n- Win rate: ${winRate}% | ASP: INR ${asp.toLocaleString('en-IN')}\n- ${pending.length} pending | ${reqs.filter(r=>r.status==='Rejected').length} rejected\n\nPortfolio Health:\n- ${state.assets.length} assets | ${[...new Set(state.assets.map(a=>a.region))].length} regions\n- Avg occupancy: ${avgOcc}% (target 55%) ${avgOcc>=55?'[Above target]':'[Below target]'}\n- ${hi.length} high demand | ${state.assets.filter(a=>a.status==='Available').length} available | ${lo.length} low demand\n- ${state.benchmarks.length} benchmarks | ${uncov.length} assets without PPU coverage\n\nTop actions: ${uncov.length>0?'expand PPU coverage + ':''}${hi.length>0?'rate uplift on high-demand assets + ':''}${lo.length>0?'promotions for low-demand assets':'maintain current performance'}.`;
}

async function askCopilot(preset){
  const box=document.getElementById('cop-box');
  const q=preset||(box?box.value.trim():'');if(!q)return;
  copilotHistory.push({role:'user',text:q});if(box)box.value='';
  renderCopilot(document.getElementById('main'));
  const log=document.getElementById('cop-log');
  if(log){log.innerHTML+=`<div class="msg msg-ai typing-dots" id="typ-ind"><span></span><span></span><span></span></div>`;log.scrollTop=log.scrollHeight;}
  await new Promise(r=>setTimeout(r,600+Math.random()*500));
  const answer=generateCopilotResponse(q);
  document.getElementById('typ-ind')?.remove();
  copilotHistory.push({role:'ai',text:answer});
  renderCopilot(document.getElementById('main'));
}

/* ---- ROADMAP ---- */
function renderRoadmap(m){
  const phases=[
    {n:'1',color:'#2F5EFF',bg:'#E9EDFF',label:'Foundation',status:'Live',sc:'chip-green',q:'Q1-Q2 2025',items:['Price Point Universe master benchmark repository','Benchmark-first pricing engine with confidence scoring','Intelligent fallback pricing (traffic/reach/occupancy model)','Role-based access control across 5 user personas','Commercial approval workflow with governance','Immutable audit trail and full decision traceability','Asset catalogue management (12 assets, 4 regions, 5 classes)']},
    {n:'2',color:'#0F8A55',bg:'#E4F6EC',label:'Intelligence',status:'In Progress',sc:'chip-amber',q:'Q3-Q4 2025',items:['Executive dashboards with 4 KPIs and 4 live charts','Financial Feasibility Engine (ROI, IRR, NPV, payback, MAG)','Scenario Planning with 3 strategy modes and comparison charts','Market Insights with 6 auto-generated portfolio intelligence cards','Commercial Intelligence Assistant grounded in live data','Filterable asset and PPU explorer with CSV audit export','Add asset and benchmark forms with audit logging']},
    {n:'3',color:'#C6821F',bg:'#FBF0DD',label:'AI Enablement',status:'Planned',sc:'chip-grey',q:'Q1-Q2 2026',items:['Pricing Intelligence and Revenue Optimization agents','Occupancy Forecasting and demand prediction engine','Financial Analysis engine with scenario generation','Semantic search over pricing history','Customer and asset knowledge graph','Commercial model gateway','API Gateway and OAuth2/OIDC authentication layer']},
    {n:'4',color:'#7C3AED',bg:'#EDE9FE',label:'Autonomy',status:'Roadmap',sc:'chip-purple',q:'Q3-Q4 2026',items:['Autonomous revenue optimization and real-time price adjustment','Predictive pricing with reinforcement learning feedback loop','Event-driven microservices architecture','Enterprise data lakehouse persistence','Kubernetes deployment with auto-scaling and zero-downtime rollout','DevSecOps: SAST, dependency scanning, IaC validation','Enterprise cloud routing architecture']},
  ];
  m.innerHTML=`
    <div class="topbar"><div class="topbar-left"><h2>Platform Roadmap</h2><p>Phased evolution from rule-based pricing foundation to autonomous revenue optimization</p></div></div>
    <div class="card" style="margin-bottom:18px;">
      <div class="section-title">Delivery Timeline</div>
      <div class="timeline-bar">${phases.map(p=>`<div class="timeline-seg" style="background:${p.color};opacity:${p.status==='Live'?1:p.status==='In Progress'?.65:.3};" title="${p.label} — ${p.q}"></div>`).join('')}</div>
      <div style="display:flex;justify-content:space-between;margin-top:8px;font-size:11px;color:var(--text-dim);">${phases.map(p=>`<span>${p.q}</span>`).join('')}</div>
      <div style="display:flex;gap:16px;margin-top:12px;font-size:12px;flex-wrap:wrap;">
        <span><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--green);margin-right:5px;"></span>Live</span>
        <span><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--amber);margin-right:5px;"></span>In Progress</span>
        <span><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#D5D9E3;margin-right:5px;"></span>Planned / Roadmap</span>
      </div>
    </div>
    <div class="grid grid-2">${phases.map(p=>`<div class="phase-card card-hover"><div class="phase-header" style="background:${p.bg};"><div class="phase-num" style="background:${p.color};color:#fff;">P${p.n}</div><div><div style="font-weight:700;font-size:15px;color:${p.color};">${p.label}</div><div style="font-size:12px;color:var(--text-dim);margin-top:2px;">${p.q}</div></div><div style="margin-left:auto;"><span class="chip ${p.sc}">${p.status}</span></div></div><div class="phase-body">${p.items.map(item=>`<div class="phase-item" style="color:${p.color};"><div class="phase-dot" style="background:${p.color};"></div><span style="color:var(--ink);">${item}</span></div>`).join('')}</div></div>`).join('')}</div>
    <div class="card" style="margin-top:18px;"><div class="section-title">Architecture Stack (Production Target)</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;">${[['01','API & Auth','Kong Gateway, OAuth2/OIDC, RBAC, HashiCorp Vault'],['02','Data','PostgreSQL, Iceberg/Trino, MinIO, Redis, Apache Kafka'],['03','Intelligence Layer','Optimization Engine, Lite Gateway, Qdrant, Neo4j, OpenSearch'],['04','Infrastructure','Kubernetes/RKE2, HPA, GitHub Actions, DevSecOps']].map(([ic,t,d])=>`<div class="insight-card"><div class="insight-icon">${ic}</div><div class="insight-body"><h4>${t}</h4><p>${d}</p></div></div>`).join('')}</div></div>`;
}

/* INIT */
renderRoleGrid();
</script>
</body>
</html>
""")

content = ''.join(PARTS)

out_index = os.path.join(WORKDIR, "index.html")
out_platform = os.path.join(WORKDIR, "PIROP-Platform.html")

with open(out_index, "w", encoding="utf-8") as f:
    f.write(content)

with open(out_platform, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated clean index.html: {os.path.getsize(out_index):,} bytes")
print(f"Generated clean PIROP-Platform.html: {os.path.getsize(out_platform):,} bytes")
