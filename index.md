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

{% if post.categories or post.tags %}
  <div class="dossier-meta">
    {% if post.categories %}
      {% for c in post.categories %}
        <span class="dossier-chip dossier-chip-cat">{{ c }}</span>
      {% endfor %}
    {% endif %}

    {% if post.tags %}
      {% for t in post.tags %}
        <span class="dossier-chip dossier-chip-tag">{{ t }}</span>
      {% endfor %}
    {% endif %}
  </div>
{% endif %}

      </article>
    {% endfor %}
  </div>
</section>
