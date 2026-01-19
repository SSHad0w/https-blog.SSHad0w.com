---
layout: default
title: Log Files
---

<section class="home">
  <div class="home-head">
    <h1 class="home-title">{{ site.title }}</h1>
    <p class="home-sub">
      Notes, writeups, and system autopsies.
    </p>
  </div>

  <div class="dossier-list">
    {% for post in site.posts %}
      <article class="dossier">
        <div class="dossier-top">
          <h2 class="dossier-title">
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          </h2>

          <time class="dossier-date" datetime="{{ post.date | date_to_xmlschema }}">
            {{ post.date | date: "%Y-%m-%d" }}
          </time>
        </div>

        {% if post.excerpt %}
          <p class="dossier-excerpt">{{ post.excerpt | strip_html | truncate: 220 }}</p>
        {% endif %}

        <div class="dossier-meta">
          <span class="dossier-chip">entry</span>
          {% if post.tags and post.tags.size > 0 %}
            <span class="dossier-chip">tagged</span>
          {% endif %}
        </div>
      </article>
    {% endfor %}
  </div>
</section>
