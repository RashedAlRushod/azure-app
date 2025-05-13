## VM vs App Service comparison

| Metric | Virtual Machine | Azure App Service |
|--------|-----------------|-------------------|
| **Cost** | Pay for entire VM 24 × 7 (e.g., B1s ≈ $25-30/mo) **on top of** disk + bandwidth; certificates extra. | Free for development (F1); production from Basic B1 ≈ $13/mo and auto-scales based on plan. OS patching and TLS certs not extra.
| **Scalability** | Manual: resize VM or add load balancer & extra VMs; bespoke scripting required. | Slider-based horizontal and vertical scaling, portal-based autoscale rules. |
| **Availability** | You patch/ reboot OS; no SLA on individual VM unless within Availability Set / Zone. | Microsoft patches OS; 99.95 % SLA on Basic+ plans; deployment slots for zero-downtime roll-outs.
| **Workflow** | SSH into VM, install Nginx, Python venv, systemd; future updates via Git pull or CI script. | Push to GitHub → App Service build → deploy; config thru portal; log stream & Kudu built-in.

## Chosen option

**Azure App Service** — it costs less at low traffic, scales automatically, and does away with OS-level maintenance. For a student CMS with bursty but low-traffic usage, paying only for the plan and letting Azure patch is simpler and more reliable than running a VM constantly. Two deployment slots also enable me to test updates safely.

## When would a VM be better?

If the app later needs **custom OS packages, daemons running in the background, or access to the GPU**, or if I have to execute Docker containers that App Service (Code) can't handle, I'd opt for a VM (or Container Apps). Also, rigid compliance that involves complete OS control or sophisticated networking (e.g., custom Nginx modules) would shift the choice to VM/AKS.