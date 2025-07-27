🚀 Project10 - Complete Monitoring Stack in Docker – Fully Automated with Ansible 🐳📊

Over the past few days, I put together a self-contained observability stack — everything custom-built from scratch using:

Docker (no Kubernetes)

Ansible for automation

Prometheus + Grafana for metrics & dashboards

Node Exporter (in container!) for system-level metrics

A custom Flask microservice exposing Prometheus metrics

A Bash-based traffic simulator to stress the service



📦 Highlights:

Node Exporter runs inside a Docker container but still exposes host/node-level CPU, memory, and disk metrics by sharing necessary namespaces.

The Flask service has a /metrics endpoint with real-time latency histograms & request counters.

Prometheus is configured to scrape from the microservice, node-exporter, and simulate alerting conditions.

Grafana visualizes everything using pre-loaded dashboards and persists data via volumes.

A small Ansible playbook spins up everything — builds Docker images, sets up the custom network, and launches all services.

The traffic simulator mimics real-world load by randomly calling fast and slow endpoints — great for generating Prometheus alerts.



🧪 Ideal for:

Learning observability in container-based environments

Simulating production-like telemetry on a dev machine

Exploring alerting, custom metrics, and automation with Docker

👨‍💻 Tech Stack:

 Docker + Ansible + Flask + Prometheus + Grafana + Bash



📁 Project Tree:

Infra-in-Docker/

├── ansible/

├── grafana/

├── microservice/

├── node-exporter/

├── prometheus/

├── traffic-simulator/



Everything is built with custom Dockerfiles and orchestrated with Ansible. No Docker Compose, no Kubernetes — just simple, modular automation.



GitHub: https://github.com/Sayantan2k24/LW-Project-10-Dockerized-Microservice-Application-with-Prometheus-and-Grafana.git



Thank you Vimal Daga sir for this project and really grateful to you for giving us the chance of exploring on this level and troubleshooting.



Let’s connect if you’re working on similar infra setups!



#Docker #Prometheus #Grafana #Flask #Monitoring #DevOps #Observability #OpenSource #Ansible #Metrics #Python #IaC