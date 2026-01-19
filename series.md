---
layout: default
title: Series
permalink: /series/
---

<section class="tags">
  <div class="home-head">
    <h1 class="home-title">Series</h1>
    <p class="home-sub">Grouped sets of posts.</p>
  </div>

  {% assign series_map = site.posts | where_exp: "p", "p.series" | group_by: "series" %}
  <div class="tag-cloud">
    {% for s in series_map %}
      <a class="tag-link" href="#{{ s.name | slugify }}">
        {{ s.name }} <span class="tag-count">{{ s.items | size }}</span>
      </a>
    {% endfor %}
  </div>

  {% for s in series_map %}
    <h2 id="{{ s.name | slugify }}" class="tag-section-title">{{ s.name }}</h2>

    <div class="dossier-list">
      {% assign ordered = s.items | sort: "series_order" %}
      {% for post in ordered %}
        <article class="dossier">
          <div class="dossier-top">
            <h3 class="dossier-title" style="font-size:16px;">
              <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            </h3>
            <time class="dossier-date" datetime="{{ post.date | date_to_xmlschema }}">
              {% if post.series_order %}Part {{ post.series_order }}{% else %}{{ post.date | date: "%Y-%m-%d" }}{% endif %}
            </time>
          </div>
          {% if post.excerpt %}
            <p class="dossier-excerpt">{{ post.excerpt | strip_html | truncate: 200 }}</p>
          {% endif %}
        </article>
      {% endfor %}
    </div>
  {% endfor %}
</section>
