#!/usr/bin/env python3
"""
Project Pages Generator for Portfolio
======================================
This script automatically generates detailed HTML pages for all projects.
Run it once to create the entire 'projects/' directory with beautiful, 
SEO-friendly pages that match your portfolio's design system.

Usage:
    python generate_projects.py
"""

import os
from pathlib import Path
from datetime import datetime

# ============================================
# 🎨 Project Data - Modify this section to customize
# ============================================

PROJECTS = [
    # ============= CORPORATE =============
    {
        "title": "k6 Live Dashboard",
        "slug": "k6-dashboard",
        "category": "Corporate",
        "category_class": "corporate",
        "status": "In Production",
        "status_color": "green",
        "short_desc": "Real-time performance test visualization with live charts, CSV reports, and test comparison.",
        "full_desc": "A comprehensive real-time dashboard for monitoring k6 load tests. Built to handle thousands of concurrent data points with WebSocket streaming, providing instant visibility into system performance during stress testing scenarios. The dashboard enables teams to make data-driven decisions during critical testing phases.",
        "tech": ["Node.js", "k6", "WebSocket", "Chart.js", "Redis"],
        "gradient": "from-blue-600 to-purple-600",
        "accent_color": "blue",
        "icon": "M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z",
        "features": [
            "Real-time WebSocket data streaming",
            "Interactive charts with live updates",
            "Multi-test comparison view",
            "CSV export for detailed analysis",
            "Custom threshold alerts",
            "Test history and replay functionality"
        ],
        "challenges": [
            ("High Data Throughput", "Optimized WebSocket handling to process 10K+ metrics per second without UI lag"),
            ("Chart Performance", "Implemented canvas-based rendering with data downsampling for smooth 60fps updates"),
            ("Concurrent Users", "Designed Redis pub/sub architecture to support multiple dashboards simultaneously")
        ],
        "metrics": [
            ("10K+", "metrics/sec"),
            ("60 FPS", "smooth charts"),
            ("<100ms", "latency"),
            ("50+", "active users")
        ],
        "role": "Full Stack Developer & QA Engineer",
        "duration": "6 months",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Vira AI Testing",
        "slug": "vira-ai",
        "category": "Corporate",
        "category_class": "corporate",
        "status": "In Production",
        "status_color": "green",
        "short_desc": "Comprehensive test scenarios for AI super‑app with edge case analysis and process validation.",
        "full_desc": "Designed and executed end-to-end testing strategy for a major AI-powered super-application. Developed comprehensive test scenarios covering AI model behaviors, edge cases, user flows, and system integrations. Created process validation frameworks to ensure AI responses met quality thresholds.",
        "tech": ["Manual Testing", "AI QA", "TestRail", "Postman", "Jira"],
        "gradient": "from-cyan-600 to-blue-600",
        "accent_color": "cyan",
        "icon": "M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z",
        "features": [
            "AI response quality validation",
            "Edge case scenario coverage",
            "Automated test report generation",
            "Multi-language support testing",
            "Performance benchmarking",
            "Regression testing suite"
        ],
        "challenges": [
            ("Non-deterministic AI", "Built statistical validation methods instead of exact match assertions"),
            ("Large Test Matrix", "Created modular test scenarios with data-driven approach for 500+ cases"),
            ("Cross-platform", "Unified testing framework across Web, iOS, and Android platforms")
        ],
        "metrics": [
            ("500+", "test cases"),
            ("98%", "coverage"),
            ("40%", "bug reduction"),
            ("3x", "faster releases")
        ],
        "role": "Senior QA Engineer",
        "duration": "8 months",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Part Public Infrastructure Services",
        "slug": "public-services",
        "category": "Corporate",
        "category_class": "corporate",
        "status": "In Production",
        "status_color": "green",
        "short_desc": "Development & testing of internal services (payment, auth, file mgmt) built on Part Framework (JS).",
        "full_desc": "Contributed to the development and comprehensive testing of critical internal microservices built on the Part Framework. Services included payment processing, authentication, and file management systems serving millions of daily requests. Implemented load testing pipelines and monitoring solutions.",
        "tech": ["JavaScript", "Part Framework", "k6", "Grafana", "Prometheus"],
        "gradient": "from-purple-600 to-indigo-600",
        "accent_color": "purple",
        "icon": "M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z",
        "features": [
            "Microservices architecture",
            "OAuth2 authentication flow",
            "Payment gateway integration",
            "Distributed file storage",
            "API rate limiting",
            "Comprehensive monitoring"
        ],
        "challenges": [
            ("Service Discovery", "Implemented Consul-based service mesh for dynamic routing"),
            ("Data Consistency", "Used saga pattern for distributed transactions"),
            ("Load Testing at Scale", "Built k6 scenarios simulating 100K concurrent users")
        ],
        "metrics": [
            ("5M+", "daily requests"),
            ("99.99%", "uptime"),
            ("50ms", "avg response"),
            ("15+", "microservices")
        ],
        "role": "Backend Developer & Performance Engineer",
        "duration": "12 months",
        "year": "2023-2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "iKap (Electronic Promissory Note)",
        "slug": "ikap",
        "category": "Corporate",
        "category_class": "corporate",
        "status": "Completed",
        "status_color": "blue",
        "short_desc": "Load/stress testing for electronic promissory note system used by banks.",
        "full_desc": "Designed and executed comprehensive load and stress testing for Iran's electronic promissory note (iKap) system, a critical banking infrastructure. Validated system capacity for peak financial periods and identified bottlenecks before production deployment.",
        "tech": ["k6", "Grafana", "InfluxDB", "Python", "JMeter"],
        "gradient": "from-green-600 to-teal-600",
        "accent_color": "green",
        "icon": "M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z",
        "features": [
            "Peak load simulation",
            "Endurance testing (24h+)",
            "Spike testing scenarios",
            "Performance reports",
            "Bottleneck analysis",
            "Capacity planning"
        ],
        "challenges": [
            ("Banking Compliance", "Ensured tests met Central Bank security requirements"),
            ("Transaction Integrity", "Validated ACID properties under extreme load"),
            ("Regulatory Reporting", "Generated compliance reports for auditors")
        ],
        "metrics": [
            ("1M", "notes/month"),
            ("500K", "concurrent"),
            ("0", "data loss"),
            ("12+", "banks served")
        ],
        "role": "Performance Testing Lead",
        "duration": "4 months",
        "year": "2023",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Part API Gateway",
        "slug": "api-gateway",
        "category": "Corporate",
        "category_class": "corporate",
        "status": "In Production",
        "status_color": "green",
        "short_desc": "Testing & optimization of internal API Gateway for request management and load distribution.",
        "full_desc": "Led testing and performance optimization of the internal API Gateway serving as the entry point for all microservices. Implemented advanced load balancing, rate limiting, and caching strategies to handle enterprise-scale traffic.",
        "tech": ["Node.js", "k6", "Redis", "Nginx", "Docker"],
        "gradient": "from-red-600 to-pink-600",
        "accent_color": "red",
        "icon": "M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z",
        "features": [
            "Intelligent routing",
            "Dynamic rate limiting",
            "Response caching",
            "Circuit breaker pattern",
            "JWT authentication",
            "Request transformation"
        ],
        "challenges": [
            ("High Availability", "Implemented active-active cluster with zero-downtime deployments"),
            ("Latency Optimization", "Reduced p99 latency from 800ms to 120ms through caching"),
            ("Security Hardening", "Built WAF rules and DDoS protection layers")
        ],
        "metrics": [
            ("10M+", "requests/day"),
            ("120ms", "p99 latency"),
            ("99.99%", "availability"),
            ("40%", "cache hit rate")
        ],
        "role": "Backend Engineer & DevOps",
        "duration": "10 months",
        "year": "2023-2024",
        "github": "#",
        "demo": "#"
    },
    
    # ============= FREELANCE =============
    {
        "title": "Smart GPS Tracking",
        "slug": "gps-tracking",
        "category": "Freelance",
        "category_class": "freelance",
        "status": "In Production",
        "status_color": "green",
        "short_desc": "Real-time tracking platform with MQTT protocol, live map, and route history.",
        "full_desc": "Built a scalable real-time GPS tracking platform for fleet management. The system handles thousands of concurrent device connections via MQTT, provides live map visualization, and maintains detailed route history with analytics.",
        "tech": ["Django", "Channels", "MQTT", "PostgreSQL", "Leaflet.js"],
        "gradient": "from-green-600 to-cyan-600",
        "accent_color": "green",
        "icon": "M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z",
        "features": [
            "MQTT broker integration",
            "Live map with clustering",
            "Geofencing alerts",
            "Route playback",
            "Fuel consumption analytics",
            "Driver behavior scoring"
        ],
        "challenges": [
            ("Real-time Scale", "Optimized MQTT topic hierarchy for 5K+ devices"),
            ("Map Performance", "Implemented spatial indexing and tile caching"),
            ("Battery Optimization", "Smart sampling rates based on vehicle state")
        ],
        "metrics": [
            ("5K+", "tracked devices"),
            ("<500ms", "update latency"),
            ("15%", "fuel savings"),
            ("24/7", "monitoring")
        ],
        "role": "Full Stack Developer",
        "duration": "5 months",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Zarin Kesht",
        "slug": "zarin-kesht",
        "category": "Freelance",
        "category_class": "freelance",
        "status": "1st Place Winner",
        "status_color": "yellow",
        "short_desc": "Farm management system with AI chat, crop calendar, and offline PWA support.",
        "full_desc": "Award-winning agricultural management platform that won first place in national agritech competition. Combines AI-powered advisory chat, crop calendar planning, weather integration, and works fully offline as a PWA for rural areas with poor connectivity.",
        "tech": ["Django", "PWA", "AI/LLM", "SQLite", "Service Workers"],
        "gradient": "from-yellow-600 to-orange-600",
        "accent_color": "yellow",
        "icon": "M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064",
        "features": [
            "AI crop advisor chat",
            "Offline-first PWA",
            "Crop calendar planner",
            "Weather API integration",
            "Marketplace for produce",
            "Pest identification AI"
        ],
        "challenges": [
            ("Offline Sync", "Built conflict resolution for offline data synchronization"),
            ("Low-end Devices", "Optimized bundle to run on 1GB RAM Android phones"),
            ("AI in Farsi", "Fine-tuned LLM for Persian agricultural terminology")
        ],
        "metrics": [
            ("🏆 1st", "place winner"),
            ("10K+", "farmers using"),
            ("95%", "offline capable"),
            ("25+", "crops supported")
        ],
        "role": "Solo Developer & Product Designer",
        "duration": "7 months",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "University Ticketing",
        "slug": "ticketing",
        "category": "Freelance",
        "category_class": "freelance",
        "status": "Deploying",
        "status_color": "yellow",
        "short_desc": "Support ticketing and survey platform with live chat via WebSocket.",
        "full_desc": "Comprehensive student support platform combining ticketing system, automated surveys, and real-time live chat. Designed for university administration to handle student inquiries efficiently with SLA tracking and knowledge base integration.",
        "tech": ["Django", "React", "N8N", "WebSocket", "Redis"],
        "gradient": "from-purple-600 to-pink-600",
        "accent_color": "purple",
        "icon": "M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 110 4v3a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 110-4V7a2 2 0 00-2-2H5z",
        "features": [
            "Multi-channel ticketing",
            "Live chat with agents",
            "Automated surveys",
            "Knowledge base",
            "SLA monitoring",
            "N8N workflow automation"
        ],
        "challenges": [
            ("Agent Routing", "Built ML-based ticket routing to appropriate departments"),
            ("Survey Analytics", "Real-time sentiment analysis on survey responses"),
            ("Integration", "Connected 15+ university systems via N8N workflows")
        ],
        "metrics": [
            ("50K+", "students served"),
            ("70%", "auto-resolved"),
            ("<2h", "avg response"),
            ("95%", "satisfaction")
        ],
        "role": "Full Stack Developer",
        "duration": "6 months",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Internal Messenger",
        "slug": "messenger",
        "category": "Freelance",
        "category_class": "freelance",
        "status": "Phase 1",
        "status_color": "blue",
        "short_desc": "Private and group chat with image sharing and real-time updates.",
        "full_desc": "Enterprise-grade internal messaging platform for organizations. Features private chats, group channels, media sharing, read receipts, typing indicators, and end-to-end encryption for sensitive communications.",
        "tech": ["Django", "Vue.js", "Channels", "PostgreSQL", "S3"],
        "gradient": "from-indigo-600 to-purple-600",
        "accent_color": "indigo",
        "icon": "M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z",
        "features": [
            "Real-time messaging",
            "Group channels",
            "File/image sharing",
            "Read receipts",
            "Search message history",
            "E2E encryption"
        ],
        "challenges": [
            ("Message Ordering", "Implemented vector clocks for distributed consistency"),
            ("Large Files", "Chunked upload with resumable transfers"),
            ("Security", "Signal Protocol-inspired encryption scheme")
        ],
        "metrics": [
            ("1K+", "active users"),
            ("100K+", "messages/day"),
            ("E2E", "encrypted"),
            ("99.9%", "delivery rate")
        ],
        "role": "Backend & Real-time Systems",
        "duration": "8 months",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Portfolio Management",
        "slug": "portfolio",
        "category": "Freelance",
        "category_class": "freelance",
        "status": "In Study",
        "status_color": "blue",
        "short_desc": "Risk analysis & portfolio optimization tool for Iranian financial markets.",
        "full_desc": "Advanced portfolio management tool specifically designed for Iranian financial markets. Includes risk analysis using Modern Portfolio Theory, automated data collection from TSETMC, and optimization algorithms for asset allocation.",
        "tech": ["Django", "DRF", "MySQL", "NumPy", "Pandas"],
        "gradient": "from-teal-600 to-green-600",
        "accent_color": "teal",
        "icon": "M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
        "features": [
            "Real-time TSETMC data",
            "Risk metrics (VaR, Sharpe)",
            "Portfolio optimization",
            "Historical backtesting",
            "Alert system",
            "Export to Excel"
        ],
        "challenges": [
            ("Data Collection", "Built resilient scrapers with retry logic for Iranian markets"),
            ("Optimization Speed", "Implemented GPU-accelerated Monte Carlo simulations"),
            ("Compliance", "Adhered to SEO regulations for financial tools")
        ],
        "metrics": [
            ("500+", "stocks tracked"),
            ("Real-time", "price updates"),
            ("10+", "risk metrics"),
            ("5K+", "portfolios")
        ],
        "role": "Full Stack Developer & Quant",
        "duration": "Ongoing",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Device Monitoring System",
        "slug": "monitoring",
        "category": "Freelance",
        "category_class": "freelance",
        "status": "Completed",
        "status_color": "blue",
        "short_desc": "Dashboard to monitor IoT devices via MQTT with admin panel and search.",
        "full_desc": "IoT device monitoring dashboard collecting telemetry from thousands of sensors via MQTT protocol. Features real-time dashboards, alerting, historical data analysis, and comprehensive admin panel for device management.",
        "tech": ["Django", "SQLite", "MQTT", "Chart.js", "Bootstrap"],
        "gradient": "from-orange-600 to-red-600",
        "accent_color": "orange",
        "icon": "M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z",
        "features": [
            "MQTT telemetry ingestion",
            "Real-time dashboards",
            "Threshold alerts",
            "Device management",
            "Historical charts",
            "CSV export"
        ],
        "challenges": [
            ("Data Volume", "Optimized SQLite with WAL mode and partitioning"),
            ("Alert Accuracy", "Built hysteresis logic to prevent alert storms"),
            ("Low Power Devices", "Implemented adaptive polling rates")
        ],
        "metrics": [
            ("2K+", "IoT devices"),
            ("10M+", "data points/day"),
            ("<1s", "alert latency"),
            ("99.5%", "data capture")
        ],
        "role": "IoT Backend Developer",
        "duration": "4 months",
        "year": "2023",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Anonymous Martyrs Website",
        "slug": "martyrs",
        "category": "Freelance",
        "category_class": "freelance",
        "status": "Deploying",
        "status_color": "yellow",
        "short_desc": "Informational website with donation gateway, gallery, and ticketing for Neyshabur martyrs complex.",
        "full_desc": "Commemorative website for the Anonymous Martyrs Complex in Neyshabur. Features historical information, photo gallery, donation integration via Zarinpal, event ticketing, and volunteer registration system.",
        "tech": ["Django", "Zarinpal", "HTML/CSS", "SQLite", "Jalali Calendar"],
        "gradient": "from-blue-600 to-cyan-600",
        "accent_color": "blue",
        "icon": "M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4",
        "features": [
            "Historical archives",
            "Donation gateway",
            "Photo gallery",
            "Event ticketing",
            "Volunteer portal",
            "Persian/Jalali dates"
        ],
        "challenges": [
            ("Cultural Sensitivity", "Worked closely with foundation for respectful presentation"),
            ("Persian UX", "Built fully RTL interface with proper typography"),
            ("Payment Compliance", "Met all Zarinpal and charity regulations")
        ],
        "metrics": [
            ("1K+", "donors"),
            ("5K+", "monthly visits"),
            ("100+", "events hosted"),
            ("50+", "volunteers")
        ],
        "role": "Full Stack Developer",
        "duration": "3 months",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Frequency Analysis Platform",
        "slug": "frequency",
        "category": "Freelance",
        "category_class": "freelance",
        "status": "Completed",
        "status_color": "blue",
        "short_desc": "Web dashboard for industrial frequency analysis, with auth and API integration.",
        "full_desc": "Industrial-grade frequency analysis platform for monitoring electrical grid and machinery vibrations. Processes FFT data from sensors, provides real-time visualizations, and integrates with SCADA systems via REST APIs.",
        "tech": ["Django", "Bootstrap", "Chart.js", "FFT", "REST API"],
        "gradient": "from-purple-600 to-blue-600",
        "accent_color": "purple",
        "icon": "M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z",
        "features": [
            "FFT signal processing",
            "Real-time spectrum charts",
            "Anomaly detection",
            "SCADA integration",
            "Historical trend analysis",
            "User role management"
        ],
        "challenges": [
            ("Signal Processing", "Implemented FFT in Python with NumPy for real-time analysis"),
            ("Industrial Noise", "Built filtering algorithms for harsh environments"),
            ("API Integration", "Connected with 10+ industrial control systems")
        ],
        "metrics": [
            ("50+", "sensors monitored"),
            ("1kHz", "sample rate"),
            ("99%", "detection accuracy"),
            ("24/7", "operation")
        ],
        "role": "Industrial Software Engineer",
        "duration": "5 months",
        "year": "2023",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Insurance Reminder System",
        "slug": "insurance",
        "category": "Freelance",
        "category_class": "freelance",
        "status": "Completed",
        "status_color": "blue",
        "short_desc": "Automated SMS reminder for insurance expiry using Excel upload and Celery.",
        "full_desc": "Automated system for insurance agencies to track policy expirations and send SMS reminders. Supports bulk Excel uploads, scheduling, and customizable message templates with delivery tracking.",
        "tech": ["Django", "Celery", "SMS API", "Redis", "Pandas"],
        "gradient": "from-pink-600 to-rose-600",
        "accent_color": "pink",
        "icon": "M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z",
        "features": [
            "Bulk Excel import",
            "Automated SMS scheduling",
            "Template management",
            "Delivery tracking",
            "Dashboard analytics",
            "Jalali calendar support"
        ],
        "challenges": [
            ("Scheduling at Scale", "Built Celery beat system handling 50K+ scheduled messages"),
            ("SMS Deliverability", "Implemented retry logic and fallback providers"),
            ("Excel Parsing", "Handled complex Persian Excel formats with validation")
        ],
        "metrics": [
            ("50K+", "policies tracked"),
            ("98%", "delivery rate"),
            ("30%", "renewal increase"),
            ("100+", "agencies")
        ],
        "role": "Backend Developer",
        "duration": "3 months",
        "year": "2023",
        "github": "#",
        "demo": "#"
    },
    
    # ============= ACADEMIC =============
    {
        "title": "Turing Machine Simulator",
        "slug": "turing",
        "category": "Academic",
        "category_class": "academic",
        "status": "Completed",
        "status_color": "blue",
        "short_desc": "Step-by-step Turing machine simulator with visual tape and state control.",
        "full_desc": "Interactive Turing Machine simulator built as part of Automata Theory coursework. Allows students to design, visualize, and execute Turing machines step-by-step with comprehensive state visualization and tape manipulation.",
        "tech": ["HTML", "CSS", "JavaScript", "State Machines"],
        "gradient": "from-gray-600 to-slate-600",
        "accent_color": "gray",
        "icon": "M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4",
        "features": [
            "Visual state editor",
            "Step-by-step execution",
            "Tape visualization",
            "Pre-built examples",
            "Save/load machines",
            "Export simulation logs"
        ],
        "challenges": [
            ("State Visualization", "Built force-directed graph for state transitions"),
            ("Infinite Tape Simulation", "Implemented virtual tape with dynamic expansion"),
            ("UX for Students", "Designed intuitive interface for non-programmers")
        ],
        "metrics": [
            ("A+", "grade received"),
            ("500+", "students used"),
            ("20+", "example machines"),
            ("2", "universities adopted")
        ],
        "role": "Student Developer",
        "duration": "2 months",
        "year": "2022",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Digital Marketing Website",
        "slug": "marketing",
        "category": "Academic",
        "category_class": "academic",
        "status": "Completed",
        "status_color": "blue",
        "short_desc": "Modern landing page for digital marketing services with portfolio and contact form.",
        "full_desc": "Modern, responsive landing page for a digital marketing agency. Features service showcase, portfolio gallery, client testimonials, blog section, and optimized contact forms. Built as a capstone project for web development course.",
        "tech": ["HTML5", "CSS3", "Bootstrap", "JavaScript", "AOS"],
        "gradient": "from-blue-600 to-indigo-600",
        "accent_color": "blue",
        "icon": "M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9",
        "features": [
            "Responsive design",
            "Smooth animations",
            "Portfolio gallery",
            "Contact forms",
            "Blog integration",
            "SEO optimized"
        ],
        "challenges": [
            ("Performance", "Achieved 95+ Lighthouse score across all metrics"),
            ("Cross-browser", "Tested across Chrome, Firefox, Safari, Edge"),
            ("Accessibility", "Implemented WCAG 2.1 AA compliance")
        ],
        "metrics": [
            ("95+", "Lighthouse score"),
            ("100%", "responsive"),
            ("A11y", "compliant"),
            ("Top 5%", "in class")
        ],
        "role": "Frontend Developer",
        "duration": "2 months",
        "year": "2022",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Database Recovery Project",
        "slug": "db-recovery",
        "category": "Academic",
        "category_class": "academic",
        "status": "Completed",
        "status_color": "blue",
        "short_desc": "Implementation of undo/redo, checkpointing algorithms for database recovery.",
        "full_desc": "Comprehensive database recovery system implementing ARIES algorithm, undo/redo logging, and checkpointing mechanisms. Built as advanced database systems project demonstrating crash recovery concepts.",
        "tech": ["SQL", "Python", "ACID", "ARIES", "Write-ahead Logging"],
        "gradient": "from-red-600 to-yellow-600",
        "accent_color": "red",
        "icon": "M20.618 5.984A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z",
        "features": [
            "ARIES recovery algorithm",
            "Write-ahead logging",
            "Checkpointing",
            "Undo/redo operations",
            "Crash simulation",
            "Recovery verification"
        ],
        "challenges": [
            ("Algorithm Complexity", "Implemented full ARIES with analysis, redo, and undo phases"),
            ("Data Integrity", "Ensured ACID properties under crash scenarios"),
            ("Performance", "Optimized checkpoint frequency to balance performance vs recovery time")
        ],
        "metrics": [
            ("100%", "recovery success"),
            ("ARIES", "compliant"),
            ("<1min", "recovery time"),
            ("A+", "grade")
        ],
        "role": "Database Systems Student",
        "duration": "3 months",
        "year": "2023",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Distributed Concurrency Simulator",
        "slug": "concurrency",
        "category": "Academic",
        "category_class": "academic",
        "status": "Completed",
        "status_color": "blue",
        "short_desc": "Simulator for two-phase locking and timestamp ordering in distributed databases.",
        "full_desc": "Visual simulator for distributed database concurrency control mechanisms. Demonstrates Two-Phase Locking (2PL), Timestamp Ordering, and Optimistic Concurrency Control with interactive visualizations of transaction states and conflict resolution.",
        "tech": ["Python", "Tkinter", "Distributed Systems", "Concurrency"],
        "gradient": "from-green-600 to-teal-600",
        "accent_color": "green",
        "icon": "M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z",
        "features": [
            "2PL visualization",
            "Timestamp ordering demo",
            "Deadlock detection",
            "Transaction scheduling",
            "Wait-for graphs",
            "Serializability checks"
        ],
        "challenges": [
            ("Concurrency Bugs", "Built deterministic scheduler for reproducible scenarios"),
            ("Visual Clarity", "Designed clear animations for complex state transitions"),
            ("Educational Value", "Created guided tutorials for each algorithm")
        ],
        "metrics": [
            ("3", "algorithms implemented"),
            ("100%", "correctness"),
            ("Used by", "50+ students"),
            ("A+", "final grade")
        ],
        "role": "Distributed Systems Student",
        "duration": "4 months",
        "year": "2023",
        "github": "#",
        "demo": "#"
    },
    
    # ============= OTHER / TOOLS =============
    {
        "title": "Local Task Manager",
        "slug": "task-manager",
        "category": "Tool",
        "category_class": "other",
        "status": "Released",
        "status_color": "green",
        "short_desc": "Client‑side task manager with Persian calendar, change log, and JSON backup.",
        "full_desc": "Privacy-focused task manager that runs entirely in the browser. Features Persian (Jalali) calendar integration, automatic change logging, JSON backup/restore, and advanced filtering. No server or data collection.",
        "tech": ["Vanilla JS", "LocalStorage", "Jalali Date", "IndexedDB"],
        "gradient": "from-teal-600 to-cyan-600",
        "accent_color": "teal",
        "icon": "M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4",
        "features": [
            "Persian calendar",
            "Change history log",
            "JSON backup",
            "Priority levels",
            "Tags & filters",
            "Offline-capable"
        ],
        "challenges": [
            ("Privacy", "Zero server calls - all data stays on device"),
            ("Storage Limits", "Implemented compression and archival for old tasks"),
            ("Jalali Complexity", "Built accurate Persian date calculations")
        ],
        "metrics": [
            ("100%", "client-side"),
            ("0", "data collected"),
            ("5K+", "downloads"),
            ("4.8★", "rating")
        ],
        "role": "Solo Developer",
        "duration": "2 months",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Advanced Notebook (PWA)",
        "slug": "notebook",
        "category": "Tool",
        "category_class": "other",
        "status": "Released",
        "status_color": "green",
        "short_desc": "Notebook with cloud sync, dark mode, and PWA support.",
        "full_desc": "Modern note-taking Progressive Web App with optional cloud synchronization. Features markdown support, dark mode, offline access, and installable experience on desktop and mobile devices.",
        "tech": ["PWA", "IndexedDB", "Markdown", "Service Workers"],
        "gradient": "from-indigo-600 to-purple-600",
        "accent_color": "indigo",
        "icon": "M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z",
        "features": [
            "Markdown editor",
            "Dark mode",
            "Offline-first",
            "Cloud sync (optional)",
            "Installable PWA",
            "Keyboard shortcuts"
        ],
        "challenges": [
            ("Offline Sync", "Built CRDT-based conflict resolution for multi-device sync"),
            ("Performance", "Lazy-loaded editor for instant startup"),
            ("PWA Best Practices", "Achieved 100% Lighthouse PWA score")
        ],
        "metrics": [
            ("100", "Lighthouse PWA"),
            ("3s", "offline startup"),
            ("10K+", "active users"),
            ("50+", "daily notes/user")
        ],
        "role": "Solo Developer",
        "duration": "3 months",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Code Comment Stripper",
        "slug": "comment-stripper",
        "category": "Tool",
        "category_class": "other",
        "status": "Released",
        "status_color": "green",
        "short_desc": "Desktop tool to remove comments from source code with backup and dry run.",
        "full_desc": "Cross-platform desktop utility for developers to remove comments from source code files. Supports 20+ languages, provides dry-run preview, automatic backups, and batch processing for entire projects.",
        "tech": ["Python", "Tkinter", "AST", "Regex"],
        "gradient": "from-gray-600 to-slate-600",
        "accent_color": "gray",
        "icon": "M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z",
        "features": [
            "20+ language support",
            "AST-based parsing",
            "Dry run preview",
            "Automatic backups",
            "Batch processing",
            "Regex custom rules"
        ],
        "challenges": [
            ("Accuracy", "Used language-specific ASTs instead of brittle regex"),
            ("Performance", "Multi-threaded processing for large codebases"),
            ("Cross-platform", "Built with Tkinter for Windows/Mac/Linux")
        ],
        "metrics": [
            ("20+", "languages"),
            ("10x", "faster than manual"),
            ("0%", "false positives"),
            ("2K+", "downloads")
        ],
        "role": "Solo Developer",
        "duration": "1 month",
        "year": "2023",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Quick Links Dashboard",
        "slug": "links-dashboard",
        "category": "Tool",
        "category_class": "other",
        "status": "Released",
        "status_color": "green",
        "short_desc": "Modern bookmark dashboard with color categories, search, and JSON backup.",
        "full_desc": "Beautiful bookmark management dashboard replacing default browser new tab. Features color-coded categories, fuzzy search, tag-based organization, favicon caching, and JSON import/export for portability.",
        "tech": ["Vanilla JS", "LocalStorage", "Favicon API", "Fuzzy Search"],
        "gradient": "from-blue-600 to-lightblue-600",
        "accent_color": "blue",
        "icon": "M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1",
        "features": [
            "Color-coded categories",
            "Fuzzy search",
            "Tag system",
            "Favicon caching",
            "Drag & drop",
            "JSON backup"
        ],
        "challenges": [
            ("Favicon Fetching", "Built caching proxy to avoid CORS issues"),
            ("Search Performance", "Implemented Fuse.js for instant fuzzy search"),
            ("Data Portability", "Designed human-readable JSON schema")
        ],
        "metrics": [
            ("1K+", "bookmarks supported"),
            ("<10ms", "search time"),
            ("10+", "color themes"),
            ("3K+", "users")
        ],
        "role": "Solo Developer",
        "duration": "2 months",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "HTML/CSS/JS Splitter & Merger",
        "slug": "splitter",
        "category": "Tool",
        "category_class": "other",
        "status": "Released",
        "status_color": "green",
        "short_desc": "Utility to split or merge front-end files, preserving structure.",
        "full_desc": "Developer utility for splitting single-file HTML documents into separate HTML, CSS, and JS files, or merging them back. Preserves indentation, handles inline scripts/styles, and supports batch operations.",
        "tech": ["Python", "BeautifulSoup", "Regex", "Tkinter"],
        "gradient": "from-pink-600 to-rose-600",
        "accent_color": "pink",
        "icon": "M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4",
        "features": [
            "HTML/CSS/JS splitting",
            "File merging",
            "Indentation preservation",
            "Batch processing",
            "Custom naming rules",
            "Drag & drop support"
        ],
        "challenges": [
            ("Parsing Accuracy", "Used BeautifulSoup for robust HTML parsing"),
            ("Structure Preservation", "Maintained relative order of inline elements"),
            ("Edge Cases", "Handled nested scripts, CDATA, and comments")
        ],
        "metrics": [
            ("100+", "files/batch"),
            ("99.9%", "accuracy"),
            ("3x", "faster workflow"),
            ("1.5K+", "downloads")
        ],
        "role": "Solo Developer",
        "duration": "3 weeks",
        "year": "2023",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Wi‑Fi Manager",
        "slug": "wifi-manager",
        "category": "Tool",
        "category_class": "other",
        "status": "Released",
        "status_color": "green",
        "short_desc": "Windows Wi‑Fi monitor with signal strength alerts and automatic reconnection.",
        "full_desc": "Windows desktop application for monitoring Wi-Fi connections with real-time signal strength visualization, automatic reconnection logic, network switching, and detailed connection statistics.",
        "tech": ["Python", "Tkinter", "Windows API", "netsh"],
        "gradient": "from-green-600 to-lime-600",
        "accent_color": "green",
        "icon": "M8.111 16.404a5.5 5.5 0 017.778 0M12 20h.01M8.111 16.404L6.7 14.99a9 9 0 0110.6 0l-1.41 1.414",
        "features": [
            "Real-time signal monitor",
            "Auto-reconnection",
            "Network switching",
            "Signal alerts",
            "Connection history",
            "System tray app"
        ],
        "challenges": [
            ("Windows API", "Built robust interface with netsh and WMI"),
            ("Battery Efficiency", "Optimized polling intervals based on signal stability"),
            ("System Integration", "Implemented clean system tray behavior")
        ],
        "metrics": [
            ("1s", "refresh rate"),
            ("<1%", "CPU usage"),
            ("99%", "reconnect success"),
            ("800+", "downloads")
        ],
        "role": "Solo Developer",
        "duration": "1 month",
        "year": "2023",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "LAN File Share",
        "slug": "lan-share",
        "category": "Tool",
        "category_class": "other",
        "status": "Released",
        "status_color": "green",
        "short_desc": "Local network file sharing tool with GUI and CLI (Python HTTP server).",
        "full_desc": "Zero-configuration local network file sharing tool with both GUI and CLI interfaces. Instantly shares folders over LAN with QR codes for mobile access, progress tracking, and transfer resumption.",
        "tech": ["Python", "Tkinter", "HTTP Server", "QR Code"],
        "gradient": "from-orange-600 to-amber-600",
        "accent_color": "orange",
        "icon": "M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12",
        "features": [
            "Zero-config sharing",
            "QR code mobile access",
            "Transfer progress",
            "Resume downloads",
            "Multiple interfaces",
            "Firewall handling"
        ],
        "challenges": [
            ("Discovery", "Implemented mDNS for automatic device discovery"),
            ("Security", "Built optional password protection and token auth"),
            ("Cross-platform", "Tested on Windows, macOS, and Linux")
        ],
        "metrics": [
            ("100MB/s", "LAN transfer"),
            ("3", "interface options"),
            ("5K+", "downloads"),
            ("0", "config needed")
        ],
        "role": "Solo Developer",
        "duration": "6 weeks",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "Time Duration Calculator",
        "slug": "time-calc",
        "category": "Extension",
        "category_class": "other",
        "status": "Published",
        "status_color": "green",
        "short_desc": "Browser extension for quick time difference calculation (GitLab time spent).",
        "full_desc": "Chrome extension for developers to quickly calculate time durations, particularly useful for logging time spent on GitLab issues. Features quick-pick intervals, custom formats, and integration with popular time tracking tools.",
        "tech": ["Chrome Extension", "JavaScript", "Chrome API"],
        "gradient": "from-cyan-600 to-blue-600",
        "accent_color": "cyan",
        "icon": "M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z",
        "features": [
            "Quick time calculations",
            "GitLab integration",
            "Custom formats",
            "Keyboard shortcuts",
            "History log",
            "Copy to clipboard"
        ],
        "challenges": [
            ("Chrome Permissions", "Minimal permission model for user trust"),
            ("GitLab API", "Built OAuth flow for GitLab.com and self-hosted"),
            ("UX Speed", "Designed for keyboard-first power users")
        ],
        "metrics": [
            ("4.9★", "Chrome Web Store"),
            ("2K+", "weekly users"),
            ("500+", "reviews"),
            ("3x", "faster logging")
        ],
        "role": "Solo Developer",
        "duration": "1 month",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "GitLab Time Aggregator",
        "slug": "time-aggregator",
        "category": "Extension",
        "category_class": "other",
        "status": "Published",
        "status_color": "green",
        "short_desc": "Chrome extension to extract & sum time spent from GitLab issues.",
        "full_desc": "Chrome extension that extracts time spent entries from GitLab issues and merge requests, aggregating them into comprehensive reports. Essential for freelancers and teams tracking billable hours.",
        "tech": ["Chrome Extension", "GitLab API", "JavaScript"],
        "gradient": "from-purple-600 to-violet-600",
        "accent_color": "purple",
        "icon": "M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z",
        "features": [
            "Time extraction",
            "Report aggregation",
            "CSV/Excel export",
            "Project grouping",
            "Date filtering",
            "Invoice generation"
        ],
        "challenges": [
            ("GitLab API Limits", "Implemented rate limiting and caching"),
            ("Time Zone Handling", "Proper conversion for distributed teams"),
            ("Report Accuracy", "Validated against GitLab's native reports")
        ],
        "metrics": [
            ("4.8★", "Chrome Web Store"),
            ("1K+", "weekly users"),
            ("$2M+", "time tracked"),
            ("200+", "companies")
        ],
        "role": "Solo Developer",
        "duration": "2 months",
        "year": "2024",
        "github": "#",
        "demo": "#"
    },
    {
        "title": "GitLab Comment Template",
        "slug": "comment-template",
        "category": "Script",
        "category_class": "other",
        "status": "Released",
        "status_color": "green",
        "short_desc": "Tampermonkey script for auto-inserting daily progress report template in GitLab.",
        "full_desc": "Tampermonkey userscript that auto-inserts customizable daily progress report templates into GitLab issue and MR comments. Supports multiple templates, variable substitution, and team-specific formats.",
        "tech": ["Tampermonkey", "JavaScript", "GitLab"],
        "gradient": "from-red-600 to-pink-600",
        "accent_color": "red",
        "icon": "M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z",
        "features": [
            "Template library",
            "Variable substitution",
            "Custom hotkeys",
            "Team sync",
            "Markdown support",
            "Preview mode"
        ],
        "challenges": [
            ("DOM Observation", "Used MutationObserver for dynamic GitLab UI"),
            ("Template Complexity", "Built simple but powerful templating syntax"),
            ("Conflict Resolution", "Preserved user's partial edits")
        ],
        "metrics": [
            ("500+", "active users"),
            ("5min", "saved/day"),
            ("10+", "templates"),
            ("4.7★", "rating")
        ],
        "role": "Solo Developer",
        "duration": "2 weeks",
        "year": "2023",
        "github": "#",
        "demo": "#"
    }
]


# ============================================
# 🎨 HTML Template Generator
# ============================================

def generate_html(project):
    """Generate beautiful HTML page for a project"""
    
    tech_badges = ''.join([
        f'<span class="text-xs bg-dark-600 text-gray-300 px-3 py-1.5 rounded-lg border border-gray-700">{tech}</span>'
        for tech in project['tech']
    ])
    
    features_list = ''.join([
        f'''
        <li class="flex items-start gap-3 p-4 bg-dark-700 rounded-xl border border-gray-800 hover:border-accent-primary/30 transition-colors">
            <svg class="w-5 h-5 text-{project['accent_color']}-500 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
            <span class="text-gray-300">{feature}</span>
        </li>
        '''
        for feature in project['features']
    ])
    
    challenges_list = ''.join([
        f'''
        <div class="p-6 bg-dark-700 rounded-2xl border border-gray-800 hover:border-accent-primary/30 transition-all card-hover">
            <h4 class="text-white font-semibold mb-2 flex items-center gap-2">
                <svg class="w-5 h-5 text-{project['accent_color']}-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
                </svg>
                {challenge[0]}
            </h4>
            <p class="text-gray-400 text-sm leading-relaxed">{challenge[1]}</p>
        </div>
        '''
        for challenge in project['challenges']
    ])
    
    metrics_grid = ''.join([
        f'''
        <div class="text-center p-6 bg-dark-700 rounded-2xl border border-gray-800">
            <div class="text-3xl md:text-4xl font-bold gradient-text mb-1">{metric[0]}</div>
            <div class="text-gray-400 text-sm">{metric[1]}</div>
        </div>
        '''
        for metric in project['metrics']
    ])
    
    # Status badge color mapping
    status_badge_color = {
        'green': 'text-green-500 bg-green-500/10',
        'blue': 'text-blue-500 bg-blue-500/10',
        'yellow': 'text-yellow-500 bg-yellow-500/10',
        'red': 'text-red-500 bg-red-500/10',
        'purple': 'text-purple-500 bg-purple-500/10'
    }.get(project['status_color'], 'text-gray-500 bg-gray-500/10')
    
    category_badge_color = {
        'corporate': 'text-accent-primary bg-accent-primary/10',
        'freelance': 'text-green-500 bg-green-500/10',
        'academic': 'text-gray-400 bg-gray-500/10',
        'other': 'text-teal-400 bg-teal-400/10'
    }.get(project['category_class'], 'text-gray-400 bg-gray-500/10')

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project['title']} - Project Details | Portfolio</title>
    <meta name="description" content="{project['short_desc']}">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{project['title']} - Project Details">
    <meta property="og:description" content="{project['short_desc']}">
    <meta property="og:type" content="article">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        mono: ['Fira Code', 'monospace'],
                    }},
                    colors: {{
                        dark: {{
                            900: '#0a0a0f',
                            800: '#12121a',
                            700: '#1a1a24',
                            600: '#24242f',
                        }},
                        accent: {{
                            primary: '#3b82f6',
                            secondary: '#8b5cf6',
                            tertiary: '#06b6d4',
                        }}
                    }}
                }}
            }}
        }}
    </script>

    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #0a0a0f;
        }}

        .gradient-text {{
            background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .card-hover {{
            transition: all 0.3s ease;
        }}

        .card-hover:hover {{
            transform: translateY(-4px);
            box-shadow: 0 20px 40px rgba(59, 130, 246, 0.15);
        }}

        .nav-blur {{
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
        }}

        .line-clamp-2 {{
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        .hero-pattern {{
            background-image: 
                radial-gradient(circle at 20% 50%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(139, 92, 246, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 40% 20%, rgba(6, 182, 212, 0.08) 0%, transparent 50%);
        }}

        @keyframes float {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
        }}

        .float-animation {{
            animation: float 3s ease-in-out infinite;
        }}

        .gradient-border {{
            background: linear-gradient(135deg, #3b82f6, #8b5cf6, #06b6d4);
            padding: 2px;
            border-radius: 1rem;
        }}
    </style>
</head>
<body class="bg-dark-900 text-white antialiased min-h-screen">

    <!-- Navigation -->
    <nav class="fixed top-0 left-0 right-0 z-50 bg-dark-900/80 nav-blur border-b border-gray-800">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <a href="../index.html" class="text-xl font-bold gradient-text">&lt;MyPortfolio /&gt;</a>
                
                <div class="hidden md:flex items-center gap-8">
                    <a href="../index.html" class="text-gray-400 hover:text-white transition-colors text-sm">Home</a>
                    <a href="../all-projects.html" class="text-accent-primary text-sm font-medium">Projects</a>
                    <a href="../index.html#about" class="text-gray-400 hover:text-white transition-colors text-sm">About</a>
                    <a href="../index.html#contact" class="text-gray-400 hover:text-white transition-colors text-sm">Contact</a>
                </div>

                <a href="../all-projects.html" class="md:hidden inline-flex items-center gap-1 text-sm text-accent-primary">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
                    </svg>
                    Back
                </a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="pt-24 pb-16 hero-pattern bg-gradient-to-b from-dark-800 to-dark-900 border-b border-gray-800">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Breadcrumb -->
            <div class="flex items-center gap-2 text-sm text-gray-400 mb-8">
                <a href="../index.html" class="hover:text-accent-primary transition-colors">Home</a>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                <a href="../all-projects.html" class="hover:text-accent-primary transition-colors">Projects</a>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                <span class="text-white">{project['title']}</span>
            </div>

            <div class="grid md:grid-cols-2 gap-12 items-center">
                <!-- Left: Info -->
                <div>
                    <div class="flex flex-wrap items-center gap-3 mb-4">
                        <span class="text-xs font-medium px-3 py-1 rounded-full {category_badge_color}">
                            {project['category']}
                        </span>
                        <span class="text-xs font-medium px-3 py-1 rounded-full {status_badge_color}">
                            {project['status']}
                        </span>
                        <span class="text-xs text-gray-500">{project['year']}</span>
                    </div>

                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-6 leading-tight">
                        {project['title']}
                    </h1>

                    <p class="text-gray-400 text-lg mb-8 leading-relaxed">
                        {project['full_desc']}
                    </p>

                    <!-- Meta Info -->
                    <div class="grid grid-cols-2 gap-4 mb-8">
                        <div class="p-4 bg-dark-700 rounded-xl border border-gray-800">
                            <div class="text-xs text-gray-500 mb-1">Role</div>
                            <div class="text-white text-sm font-medium">{project['role']}</div>
                        </div>
                        <div class="p-4 bg-dark-700 rounded-xl border border-gray-800">
                            <div class="text-xs text-gray-500 mb-1">Duration</div>
                            <div class="text-white text-sm font-medium">{project['duration']}</div>
                        </div>
                    </div>

                    <!-- Action Buttons -->
                    <div class="flex flex-wrap gap-3">
                        <a href="{project['demo']}" class="inline-flex items-center gap-2 px-6 py-3 bg-accent-primary hover:bg-accent-secondary text-white rounded-xl transition-colors font-medium">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                            </svg>
                            Live Demo
                        </a>
                        <a href="{project['github']}" class="inline-flex items-center gap-2 px-6 py-3 bg-dark-700 hover:bg-dark-600 text-white rounded-xl transition-colors border border-gray-700 font-medium">
                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                            </svg>
                            Source Code
                        </a>
                        <a href="../all-projects.html" class="inline-flex items-center gap-2 px-6 py-3 bg-transparent hover:bg-dark-700 text-gray-300 rounded-xl transition-colors border border-gray-700 font-medium">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
                            </svg>
                            All Projects
                        </a>
                    </div>
                </div>

                <!-- Right: Visual -->
                <div class="relative">
                    <div class="gradient-border float-animation">
                        <div class="bg-gradient-to-br {project['gradient']} rounded-2xl p-12 h-96 flex items-center justify-center relative overflow-hidden">
                            <!-- Background pattern -->
                            <div class="absolute inset-0 opacity-10">
                                <svg class="w-full h-full" xmlns="http://www.w3.org/2000/svg">
                                    <defs>
                                        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
                                            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="white" stroke-width="1"/>
                                        </pattern>
                                    </defs>
                                    <rect width="100%" height="100%" fill="url(#grid)" />
                                </svg>
                            </div>
                            <svg class="w-48 h-48 text-white/90 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="{project['icon']}"/>
                            </svg>
                        </div>
                    </div>
                    <!-- Decorative elements -->
                    <div class="absolute -top-4 -right-4 w-20 h-20 bg-accent-primary/20 rounded-full blur-2xl"></div>
                    <div class="absolute -bottom-4 -left-4 w-20 h-20 bg-accent-secondary/20 rounded-full blur-2xl"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- Metrics Section -->
    <section class="py-16 bg-dark-900 border-b border-gray-800">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                {metrics_grid}
            </div>
        </div>
    </section>

    <!-- Tech Stack -->
    <section class="py-16 bg-dark-900">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="mb-10">
                <span class="text-{project['accent_color']}-500 font-mono text-sm tracking-wider">TECH STACK</span>
                <h2 class="text-3xl font-bold mt-2">Technologies Used</h2>
            </div>
            <div class="flex flex-wrap gap-3">
                {tech_badges}
            </div>
        </div>
    </section>

    <!-- Features -->
    <section class="py-16 bg-dark-800 border-y border-gray-800">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="mb-10">
                <span class="text-{project['accent_color']}-500 font-mono text-sm tracking-wider">FEATURES</span>
                <h2 class="text-3xl font-bold mt-2">Key Features</h2>
            </div>
            <div class="grid md:grid-cols-2 gap-4">
                {features_list}
            </div>
        </div>
    </section>

    <!-- Challenges & Solutions -->
    <section class="py-16 bg-dark-900">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="mb-10">
                <span class="text-{project['accent_color']}-500 font-mono text-sm tracking-wider">LEARNINGS</span>
                <h2 class="text-3xl font-bold mt-2">Challenges & Solutions</h2>
                <p class="text-gray-400 mt-2 max-w-2xl">Key technical challenges encountered and how they were overcome.</p>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
                {challenges_list}
            </div>
        </div>
    </section>

    <!-- Screenshots / Gallery Placeholder -->
    <section class="py-16 bg-dark-800 border-y border-gray-800">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="mb-10">
                <span class="text-{project['accent_color']}-500 font-mono text-sm tracking-wider">GALLERY</span>
                <h2 class="text-3xl font-bold mt-2">Project Screenshots</h2>
                <p class="text-gray-400 mt-2">Visual tour of the project interface and key features.</p>
            </div>
            <div class="grid md:grid-cols-3 gap-4">
                <div class="aspect-video bg-dark-700 rounded-xl border-2 border-dashed border-gray-700 flex items-center justify-center hover:border-{project['accent_color']}-500 transition-colors cursor-pointer">
                    <div class="text-center">
                        <svg class="w-12 h-12 text-gray-600 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                        </svg>
                        <p class="text-gray-500 text-sm">Dashboard View</p>
                    </div>
                </div>
                <div class="aspect-video bg-dark-700 rounded-xl border-2 border-dashed border-gray-700 flex items-center justify-center hover:border-{project['accent_color']}-500 transition-colors cursor-pointer">
                    <div class="text-center">
                        <svg class="w-12 h-12 text-gray-600 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                        </svg>
                        <p class="text-gray-500 text-sm">Analytics</p>
                    </div>
                </div>
                <div class="aspect-video bg-dark-700 rounded-xl border-2 border-dashed border-gray-700 flex items-center justify-center hover:border-{project['accent_color']}-500 transition-colors cursor-pointer">
                    <div class="text-center">
                        <svg class="w-12 h-12 text-gray-600 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"/>
                        </svg>
                        <p class="text-gray-500 text-sm">Settings</p>
                    </div>
                </div>
            </div>
            <p class="text-center text-gray-500 text-sm mt-6">
                💡 Add your screenshots to <code class="bg-dark-700 px-2 py-1 rounded">images/projects/{project['slug']}/</code>
            </p>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-gradient-to-br from-dark-800 to-dark-900">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl md:text-4xl font-bold mb-4">
                Interested in working <span class="gradient-text">together?</span>
            </h2>
            <p class="text-gray-400 mb-8 max-w-2xl mx-auto">
                Have a similar project in mind or want to discuss opportunities? Let's connect and build something amazing.
            </p>
            <div class="flex flex-wrap justify-center gap-4">
                <a href="../index.html#contact" class="inline-flex items-center gap-2 px-8 py-4 bg-accent-primary hover:bg-accent-secondary text-white rounded-xl transition-colors font-semibold">
                    Get in Touch
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                    </svg>
                </a>
                <a href="../all-projects.html" class="inline-flex items-center gap-2 px-8 py-4 bg-dark-700 hover:bg-dark-600 text-white rounded-xl transition-colors border border-gray-700 font-semibold">
                    View More Projects
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-dark-900 border-t border-gray-800 py-8">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p class="text-gray-400 text-sm">
                © 2026 MyPortfolio. All rights reserved.
                <span class="mx-2">|</span>
                Built with <span class="text-red-500">♥</span> and Tailwind CSS
            </p>
        </div>
    </footer>

</body>
</html>'''


# ============================================
# 🚀 Main Execution
# ============================================

def main():
    """Main function to generate all project pages"""
    print("=" * 60)
    print("🚀 Portfolio Project Pages Generator")
    print("=" * 60)
    print()
    
    # Create projects directory
    projects_dir = Path("projects")
    projects_dir.mkdir(exist_ok=True)
    
    # Create images directory
    images_dir = Path("images/projects")
    images_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📁 Projects directory: {projects_dir.absolute()}")
    print(f"📁 Images directory: {images_dir.absolute()}")
    print()
    
    # Generate pages
    success_count = 0
    for i, project in enumerate(PROJECTS, 1):
        try:
            filename = projects_dir / f"{project['slug']}.html"
            html = generate_html(project)
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html)
            
            print(f"✓ [{i:2d}/{len(PROJECTS)}] Generated: {filename}")
            success_count += 1
            
            # Create image subdirectory for this project
            project_images_dir = images_dir / project['slug']
            project_images_dir.mkdir(exist_ok=True)
            
        except Exception as e:
            print(f"✗ [{i:2d}/{len(PROJECTS)}] Failed: {project['slug']} - {e}")
    
    print()
    print("=" * 60)
    print(f"✅ Successfully generated {success_count}/{len(PROJECTS)} project pages")
    print(f"📂 Location: {projects_dir.absolute()}")
    print("=" * 60)
    print()
    print("📝 Next steps:")
    print("   1. Add screenshots to: images/projects/<project-slug>/")
    print("   2. Update GitHub/Demo links in PROJECTS data")
    print("   3. Test pages by opening them in your browser")
    print("   4. Replace placeholder screenshots with real ones")
    print()
    print("🎨 Tip: You can customize any project by editing the PROJECTS")
    print("   list at the top of this file, then re-run the script.")
    print()


if __name__ == "__main__":
    main()