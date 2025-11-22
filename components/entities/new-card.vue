<template>
  <div class="blog-card" :class="{ alt: alternateLayout }">
    <div class="meta">
      <div
        class="photo"
        :style="{ backgroundImage: `url('/img/news/${instance.id}/preview.webp')` }"
        @error="handleImageError"></div>
      <div class="date-badge" v-if="instance.date">
        {{ formatDate(instance.date) }}
      </div>
    </div>
    <div class="description">
      <div class="category-tag" v-if="instance.category">
        {{ instance.category }}
      </div>
      <h1 class="card__title" v-safe-html="instance.title" />
      <h2 class="card__description" v-safe-html="instance.description" />
      <div class="card-footer">
        <p class="read-more">
          <nuxt-link :to="`/news/${instance.id}`">Читать далее</nuxt-link>
        </p>
        <div class="author" v-if="instance.author">
          <span class="author-icon">👤</span>
          {{ instance.author }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EntitiesNewCard',
  props: {
    instance: {
      type: Object,
      required: true,
      default: () => ({
        id: '',
        title: '',
        description: '',
        date: '',
        category: '',
        author: '',
      }),
    },
    alternateLayout: Boolean,
  },
  methods: {
    handleImageError(e) {
      e.target.style.backgroundImage = 'none'
      e.target.style.backgroundColor = '#f5f5f5'
      e.target.innerHTML = '<div class="image-placeholder">Колледж им. Пушкина</div>'
    },
    formatDate(dateString) {
      const options = { day: 'numeric', month: 'short', year: 'numeric' }
      return new Date(dateString).toLocaleDateString('ru-RU', options)
    },
  },
}
</script>

<style scoped lang="scss">
.blog-card {
  display: flex;
  flex-direction: column;
  margin: 0.5rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
  background: #fff;
  line-height: 1.5;
  font-family: 'Roboto', sans-serif;
  border-radius: 8px;
  overflow: hidden;
  z-index: 0;
  transition: transform 0.3s ease, box-shadow 0.3s ease;

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);

    .photo {
      transform: scale(1.05);
    }
  }

  .meta {
    position: relative;
    z-index: 0;
    height: 220px;
    overflow: hidden;

    &::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 40%;
      background: linear-gradient(to top, rgba(0, 0, 0, 0.3), transparent);
    }
  }

  .photo {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-size: cover;
    background-position: center;
    transition: transform 0.4s cubic-bezier(0.25, 0.45, 0.45, 0.95);
    background-color: #f8f9fa;

    .image-placeholder {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100%;
      color: #6c757d;
      font-size: 1.2rem;
      font-weight: 500;
      background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }
  }

  .date-badge {
    position: absolute;
    top: 15px;
    right: 15px;
    background: rgba(255, 255, 255, 0.9);
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    color: #333;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    z-index: 1;
  }

  .description {
    padding: 1.5rem;
    background: #fff;
    position: relative;
    z-index: 1;
    flex-grow: 1;
    display: flex;
    flex-direction: column;

    h1,
    h2 {
      font-family: 'Roboto', sans-serif;
    }

    .category-tag {
      display: inline-block;
      background: #3498db;
      color: white;
      padding: 3px 10px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 600;
      margin-bottom: 0.8rem;
      align-self: flex-start;
    }

    .card__title {
      line-height: 1.3;
      margin: 0 0 0.5rem 0;
      font-size: 1.5rem;
      font-weight: 600;
      color: #2c3e50;
    }

    .card__description {
      font-size: 1rem;
      font-weight: 400;
      color: #555;
      margin: 0.5rem 0 1rem;
      flex-grow: 1;
    }

    .card-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 1rem;
      padding-top: 1rem;
      border-top: 1px solid #eee;
    }

    .read-more {
      a {
        color: #c43e3e;
        display: inline-block;
        position: relative;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s;

        &:after {
          content: '→';
          margin-left: 5px;
          transition: transform 0.3s;
          display: inline-block;
        }

        &:hover {
          color: #882c2c;

          &:after {
            transform: translateX(3px);
          }
        }
      }
    }

    .author {
      font-size: 0.85rem;
      color: #7f8c8d;
      display: flex;
      align-items: center;

      .author-icon {
        margin-right: 5px;
      }
    }
  }

  @media (min-width: 768px) {
    flex-direction: row;
    max-width: 100%;

    .meta {
      flex-basis: 40%;
      height: auto;
      min-height: 250px;
    }

    .description {
      flex-basis: 60%;
      padding: 2rem;

      &:before {
        transform: skewX(-3deg);
        content: '';
        background: #fff;
        width: 30px;
        position: absolute;
        left: -10px;
        top: 0;
        bottom: 0;
        z-index: -1;
      }
    }

    &.alt {
      flex-direction: row-reverse;

      .description {
        &:before {
          left: inherit;
          right: -10px;
          transform: skew(3deg);
        }
      }
    }
  }

  @media (max-width: 767px) {
    .meta {
      height: 200px;
    }

    .description {
      padding: 1.25rem;

      .card__title {
        font-size: 1.3rem;
      }

      .card__description {
        font-size: 0.95rem;
      }
    }
  }

  @media (max-width: 480px) {
    .meta {
      height: 180px;
    }

    .description {
      padding: 1rem;

      .card__title {
        font-size: 1.2rem;
      }

      .card__description {
        font-size: 0.9rem;
      }

      .card-footer {
        flex-direction: column;
        align-items: flex-start;

        .author {
          margin-top: 0.5rem;
        }
      }
    }
  }
}
</style>
