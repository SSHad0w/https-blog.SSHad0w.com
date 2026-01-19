---
layout: default
title: Tags
permalink: /tags/
---

<section class="tags">
  <h1 class="home-title">Tags</h1>
  <p class="home-sub">Browse by label.</p>

  <div class="tag-cloud">
    {% assign sorted_tags = site.tags | sort %}
    {% for tag in sorted_tags %}
      {% assign tag_name = tag[0] %}
      {% assign tag_posts = tag[1] %}
      <a class="tag-link" href="#{{ tag_name | slugify }}">
        {{ tag_name }} <span class="tag-count">{{ tag_posts | size }}</span>
      </a>
    {% endfor %}
  </div>

  <div class="tag-sections">
    {% for tag in sorted_tags %}
      {% assign tag_name = tag[0] %}
      {% assign tag_posts = tag[1] %}
      <h2 id="{{ tag_name | slugify }}" class="tag-section-title">
        {{ tag_name }}
      </h2>

      <div class="dossier-list">
        {% for post in tag_posts %}
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
  </div>
</section>
