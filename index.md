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

        {% if post.cover %}
  <img
    class="dossier-cover{% if post.cover_size %} {{ post.cover_size }}{% endif %}"
    src="{{ post.cover | relative_url }}"
    alt=""
  >
{% endif %}


        {% if post.excerpt %}
          <p class="dossier-excerpt">{{ post.excerpt | strip_html | truncate: 220 }}</p>
        {% endif %}

        {% if post.categories or post.tags %}
          <div class="dossier-meta">
            {% if post.categories %}
              {% for c in post.categories %}
                <a class="dossier-chip dossier-chip-cat" href="{{ '/categories/#' | append: c | slugify | relative_url }}">{{ c }}</a>

              {% endfor %}
            {% endif %}

            {% if post.tags %}
              {% for t in post.tags %}
                <a class="dossier-chip dossier-chip-tag" href="{{ '/tags/#' | append: t | slugify | relative_url }}">{{ t }}</a>

              {% endfor %}
            {% endif %}
          </div>
        {% endif %}
      </article>
    {% endfor %}
  </div>
</section>
