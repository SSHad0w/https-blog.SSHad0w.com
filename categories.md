---
layout: default
title: Categories
permalink: /categories/
---

<section class="tags">
  <div class="home-head">
    <h1 class="home-title">Categories</h1>
    <p class="home-sub">Browse by bucket.</p>
  </div>

  <div class="tag-cloud">
    {% assign sorted_categories = site.categories | sort %}
    {% for cat in sorted_categories %}
      {% assign cat_name = cat[0] %}
      {% assign cat_posts = cat[1] %}
      <a class="tag-link" href="#{{ cat_name | slugify }}">
        {{ cat_name }} <span class="tag-count">{{ cat_posts | size }}</span>
      </a>
    {% endfor %}
  </div>

  {% for cat in sorted_categories %}
    {% assign cat_name = cat[0] %}
    {% assign cat_posts = cat[1] %}
    <h2 id="{{ cat_name | slugify }}" class="tag-section-title">{{ cat_name }}</h2>

    <div class="dossier-list">
      {% for post in cat_posts %}
        <article class="dossier">
          <div class="dossier-top">
            <h3 class="dossier-title" style="font-size:16px;">
              <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            </h3>
            <time class="dossier-date" datetime="{{ post.date | date_to_xmlschema }}">
              {{ post.date | date: "%Y-%m-%d" }}
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
