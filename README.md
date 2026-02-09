# SEO AI SaaS Platform

A production-grade, multi-tenant SaaS platform for automated SEO optimization using AI. Monitor, analyze, and continuously improve website SEO performance in a Google-compliant way with intelligent insights and recommendations.

## Overview

The SEO AI SaaS Platform is built as a modern monorepo combining a powerful backend service, an intelligent AI engine, and infrastructure-as-code. The platform enables teams to manage multiple organizations, projects, and websites while leveraging AI-driven SEO analysis and ranking monitoring.

### Key Features

- **Multi-Tenant Architecture**: Secure isolation between organizations with role-based access control
- **SEO Monitoring**: Track keyword rankings and website performance metrics
- **AI-Powered Analysis**: Intelligent SEO audits and optimization recommendations
- **Real-Time Data**: Live ranking data and performance insights
- **Scalable Infrastructure**: Docker-based deployment with PostgreSQL backend

---

## Tech Stack

### Backend
- **Runtime**: Node.js 20.19.0 (LTS)
- **Framework**: NestJS
- **Database**: PostgreSQL (Docker)
- **ORM**: Prisma v7
- **Package Manager**: npm

### AI Engine
- **Runtime**: Python 3.10+
- **Framework**: FastAPI
- **Dependency Management**: uv
- **Port**: 8000

### Frontend (Planned)
- React with Vite
- Tailwind CSS

### Infrastructure
- Docker + Docker Compose
- PostgreSQL container
- GitHub monorepo workflow

---

## Repository Structure

```
seo-ai-saas/
├── apps/
│   ├── backend/                 # NestJS application
│   │   ├── src/
│   │   │   ├── app.controller.ts
│   │   │   ├── app.service.ts
│   │   │   ├── app.module.ts
│   │   │   └── main.ts
│   │   ├── prisma/              # Prisma ORM configuration
│   │   │   ├── schema.prisma
│   │   │   └── migrations/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── README.md
│   ├── ai-engine/               # FastAPI AI services
│   │   ├── app/
│   │   │   └── main.py
│   │   ├── main.py
│   │   ├── pyproject.toml
│   │   └── README.md
│   └── frontend/                # React application (planned)
├── packages/                    # Shared libraries (future)
│   ├── config/
│   ├── shared-types/
│   └── ui/
├── infra/                       # Infrastructure as Code (future)
│   ├── docker/
│   ├── nginx/
│   └── terraform/
├── docs/                        # Documentation
├── scripts/                     # Utility scripts
├── docker-compose.yml           # Local development environment
├── .nvmrc                       # Node.js version specification
├── .github/                     # GitHub workflows and templates
└── README.md
```

---

## Database Schema

The platform implements a comprehensive multi-tenant schema:

### Core Entities
- **User**: System users with authentication
- **Organization**: Tenant organizations
- **Membership**: User-to-organization relationships with roles (OWNER, ADMIN, MEMBER)
- **Project**: SEO projects within organizations
- **Page**: Web pages being tracked
- **Keyword**: SEO keywords per page
- **Ranking**: Historical ranking data
- **SeoAudit**: AI-generated SEO audit reports

---

## Getting Started

### Prerequisites

- **Node.js**: 20.19.0 LTS (use `nvm` to manage versions)
- **Python**: 3.10 or higher
- **Docker**: Latest stable version
- **Docker Compose**: Latest stable version

### Node Version Management

We lock Node.js to version 20.19.0 for consistency across the team:

```bash
nvm install 20.19.0
nvm use 20.19.0
```

The version is specified in `.nvmrc` and can be activated with:
```bash
nvm use
```

---

## Database Setup

### Starting PostgreSQL

The PostgreSQL database runs in a Docker container. Start it with:

```bash
docker compose up -d
```

Verify the container is running:

```bash
docker ps
```

You should see a PostgreSQL container running on port `5432`.

### Prisma Migrations

Initialize the database schema:

```bash
cd apps/backend
npx prisma migrate deploy
```

### Prisma Studio

Explore and manage database records visually:

```bash
cd apps/backend
npx prisma studio
```

This opens an interactive dashboard at `http://localhost:5555`.

---

## Running Services

### Backend Service

Start the NestJS backend:

```bash
cd apps/backend
npm install
npm run start:dev
```

The backend runs on **http://localhost:3000** with hot-reload enabled.

### AI Engine Service

Start the FastAPI AI engine:

```bash
cd apps/ai-engine
uv sync
uv run uvicorn app.main:app --reload --port 8000
```

The AI engine runs on **http://localhost:8000** with automatic documentation available at **http://localhost:8000/docs**.

Health check endpoint: **http://localhost:8000/health**

### Full Stack (Recommended)

To run all services together:

```bash
# Terminal 1: Database
docker compose up -d

# Terminal 2: Backend
cd apps/backend
npm install
npm run start:dev

# Terminal 3: AI Engine
cd apps/ai-engine
uv sync
uv run uvicorn app.main:app --reload --port 8000
```

---

## Team Workflow

### Node Version Requirement

All team members must use Node.js 20.19.0. Verify your version:

```bash
node --version
```

Expected output: `v20.19.0`

### Branching Strategy

Follow conventional branching:
- `main` - Production-ready code
- `feature/*` - Feature development
- `fix/*` - Bug fixes

Example:
```bash
git checkout -b feature/seo-audit-api
git checkout -b fix/ranking-data-sync
```

### Monorepo Best Practices

- Work in app-specific directories (`apps/backend`, `apps/ai-engine`)
- Shared dependencies are managed per app
- Database changes must go through Prisma migrations
- Test locally across all services before committing

---

## Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes and test locally**
   - Backend: `npm run start:dev`
   - AI Engine: `uv run uvicorn app.main:app --reload`

3. **Commit with clear messages**
   ```bash
   git commit -m "feat: add seo audit endpoint"
   ```

4. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

---

## Next Steps

### Immediate Priorities
- [ ] Authentication & authorization system
- [ ] Backend CRUD endpoints for projects and pages
- [ ] Keyword ranking data integration
- [ ] SEO audit AI decision engine
- [ ] Frontend dashboard (React + Vite)

### Future Enhancements
- [ ] Advanced analytics and reporting
- [ ] Scheduled SEO audit automation
- [ ] Real-time ranking notifications
- [ ] Multi-language support
- [ ] API rate limiting and quotas
- [ ] Terraform infrastructure deployment
- [ ] GitHub Actions CI/CD pipelines

---

## Documentation

For detailed documentation on specific services:
- [Backend README](./apps/backend/README.md)
- [AI Engine README](./apps/ai-engine/README.md)

---

## Support

For questions or issues, please reach out to the development team or open an issue in the GitHub repository.

---

**Last Updated**: February 2026  
**Maintainers**: Engineering Team
