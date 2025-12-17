FROM ghcr.io/agent-infra/sandbox:latest

# Force web browsing by blocking GitHub API
# 1. Remove gh CLI
# 2. Block api.github.com (redirect to invalid IP)
RUN rm -f /usr/bin/gh /usr/local/bin/gh 2>/dev/null || true && \
    echo "127.0.0.1 api.github.com" >> /etc/hosts
