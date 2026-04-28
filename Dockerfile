FROM docker/sandbox-templates:opencode

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends just \
    && rm -rf /var/lib/apt/lists/*

USER agent
