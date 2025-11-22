<template>
  <block-ab title="Конструктор новостей">
    <div class="form">
      <div class="form__group">
        <div class="news-holder">
          <h2 class="form__title">Список всех новостей</h2>
          <button @click="selectNews(n)" v-for="(n, nIdx) of news" :key="nIdx">
            <entities-new-card :disabled="true" :instance="n" />
          </button>
        </div>
        <div class="form__controls">
          <common-input v-model="selectedOrNew.title" label="Заголовок" class="form__input" />
          <common-input v-model="selectedOrNew.slug" label="URL Slug" class="form__input" />
          <common-textarea
            v-model="selectedOrNew.description"
            rows="4"
            label="Краткое описание (для мета-тегов)"
            class="form__input" />
          <common-textarea
            v-model="selectedOrNew.content"
            rows="8"
            label="Полный текст новости"
            class="form__input" />
          <common-input v-model="selectedOrNew.image" label="URL изображения" class="form__input" />
          <common-input
            v-model="selectedOrNew.date"
            type="date"
            label="Дата публикации"
            class="form__input" />

          <div class="form__group" v-if="!isSelectedCard">
            <common-button class="form__button" @click="addNew">Добавить новость</common-button>
            <common-button class="form__button" @click="cleanForm">Очистить форму</common-button>
          </div>
          <div class="form__group" v-else>
            <common-button class="form__button" @click="saveCurrent"
              >Сохранить изменения</common-button
            >
            <common-button class="form__button" @click="deleteCurrent"
              >Удалить новость</common-button
            >
            <common-button class="form__button" @click="goBack">Назад к созданию</common-button>
          </div>

          <common-button class="form__button" @click="copyAll">
            Скопировать JSON всех новостей
          </common-button>
          <common-button class="form__button" @click="downloadNews">
            Скачать файлы новостей
          </common-button>

          <div class="news-holder">
            <h2 class="form__title" style="margin-top: 12px">Предпросмотр карточки</h2>
            <entities-new-card
              @click.native.stop.prevent="selectNews(n)"
              :instance="selectedOrNew" />
          </div>
        </div>
      </div>
    </div>

    <div class="preview-section">
      <h2 class="form__title">Предпросмотр страницы новости</h2>
      <div class="preview-content" v-safe-html="generateNewsHTML()" />
    </div>
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'

export default {
  async created() {
    try {
      this.news = JSON.parse(await loadDynamic('dynamic/news/news.json'))
    } catch {
      console.error('Проверьте валидность JSON новостей и событий!')
      // Создаем демо данные если файл не найден
      this.news = []
    }
  },

  data() {
    return {
      selectedOrNew: {
        id: null,
        slug: '',
        title: 'Заголовок новости',
        description: 'Краткое описание новости для мета-тегов',
        content: '<p>Полное содержание новости...</p>',
        image: '/images/news/default.jpg',
        date: new Date().toISOString().split('T')[0],
      },
      news: [],
    }
  },

  computed: {
    isSelectedCard() {
      return this.news.some((n) => this.selectedOrNew.id === n.id)
    },
  },

  methods: {
    generateId() {
      return Date.now() + Math.floor(Math.random() * 1000)
    },

    selectNews(nCard) {
      this.selectedOrNew = { ...nCard }
    },

    addNew() {
      if (!this.selectedOrNew.slug) {
        this.selectedOrNew.slug = this.generateSlug(this.selectedOrNew.title)
      }
      if (!this.selectedOrNew.id) {
        this.selectedOrNew.id = this.generateId()
      }

      this.news.unshift({ ...this.selectedOrNew })
      this.cleanForm()
      this.saveToLocalStorage()
    },

    generateSlug(title) {
      return title
        .toLowerCase()
        .replace(/[^\w\u0400-\u04FF]+/g, '-')
        .replace(/^-+|-+$/g, '')
        .substring(0, 50)
    },

    cleanForm() {
      this.selectedOrNew = {
        id: null,
        slug: '',
        title: 'Заголовок новости',
        description: 'Краткое описание новости для мета-тегов',
        content: '<p>Полное содержание новости...</p>',
        image: '/images/news/default.jpg',
        date: new Date().toISOString().split('T')[0],
      }
    },

    saveCurrent() {
      const currentIndex = this.news.findIndex((n) => n.id === this.selectedOrNew.id)
      if (currentIndex !== -1) {
        this.$set(this.news, currentIndex, { ...this.selectedOrNew })
        this.saveToLocalStorage()
      }
    },

    deleteCurrent() {
      this.news = this.news.filter((n) => n.id !== this.selectedOrNew.id)
      this.cleanForm()
      this.saveToLocalStorage()
    },

    goBack() {
      this.cleanForm()
    },

    copyAll() {
      const newsData = JSON.stringify(this.news, null, 2)
      navigator.clipboard
        .writeText(newsData)
        .then(() => alert('JSON скопирован в буфер обмена!'))
        .catch(() => alert('Ошибка копирования'))
    },

    saveToLocalStorage() {
      if (process.client) {
        localStorage.setItem('news-constructor-data', JSON.stringify(this.news))
      }
    },

    loadFromLocalStorage() {
      if (process.client) {
        const saved = localStorage.getItem('news-constructor-data')
        if (saved) {
          this.news = JSON.parse(saved)
        }
      }
    },

    generateNewsHTML() {
      const news = this.selectedOrNew
      return `
        <article class="news-article">
          <header class="news-header">
            <h1>${news.title || 'Заголовок новости'}</h1>
            <div class="news-meta">
              <time datetime="${news.date}">${this.formatDate(news.date)}</time>
            </div>
          </header>
          ${news.image ? `<img src="${news.image}" alt="${news.title}" class="news-image">` : ''}
          <div class="news-content">
            ${news.content || '<p>Содержание новости...</p>'}
          </div>
        </article>
      `
    },

    formatDate(dateString) {
      if (!dateString) return ''
      const date = new Date(dateString)
      return date.toLocaleDateString('ru-RU', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      })
    },

    downloadNews() {
      // Создаем JSON файл
      const jsonData = JSON.stringify(this.news, null, 2)
      const jsonBlob = new Blob([jsonData], { type: 'application/json' })
      const jsonUrl = URL.createObjectURL(jsonBlob)

      // Создаем HTML файлы для каждой новости
      const htmlFiles = this.news.map((newsItem) => {
        const htmlContent = this.generateNewsItemHTML(newsItem)
        return {
          name: `${newsItem.slug || newsItem.id}.html`,
          content: htmlContent,
        }
      })

      // Скачиваем JSON
      const jsonLink = document.createElement('a')
      jsonLink.href = jsonUrl
      jsonLink.download = 'news.json'
      jsonLink.click()

      // Скачиваем HTML файлы
      htmlFiles.forEach((file) => {
        const htmlBlob = new Blob([file.content], { type: 'text/html' })
        const htmlUrl = URL.createObjectURL(htmlBlob)
        const htmlLink = document.createElement('a')
        htmlLink.href = htmlUrl
        htmlLink.download = file.name
        htmlLink.click()
        URL.revokeObjectURL(htmlUrl)
      })

      URL.revokeObjectURL(jsonUrl)
    },

    generateNewsItemHTML(newsItem) {
      return `<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${newsItem.title} - КИТЭК</title>
    <meta name="description" content="${newsItem.description}">
    <style>
        .news-article { max-width: 800px; margin: 0 auto; padding: 20px; }
        .news-header { text-align: center; margin-bottom: 30px; }
        .news-meta { color: #666; margin-top: 10px; }
        .news-image { max-width: 100%; height: auto; margin: 20px 0; }
        .news-content { line-height: 1.6; }
    </style>
</head>
<body>
    <article class="news-article">
        <header class="news-header">
            <h1>${newsItem.title}</h1>
            <div class="news-meta">
                <time datetime="${newsItem.date}">${this.formatDate(newsItem.date)}</time>
            </div>
        </header>
        ${
          newsItem.image
            ? `<img src="${newsItem.image}" alt="${newsItem.title}" class="news-image">`
            : ''
        }
        <div class="news-content">
            ${newsItem.content}
        </div>
    </article>
</body>
</html>`
    },
  },

  mounted() {
    this.loadFromLocalStorage()
  },
}
</script>

<style scoped lang="scss">
.form {
  &__group {
    display: flex;
    width: 100%;
    gap: 0 24px;
  }
  &__controls {
    width: 100%;
    max-width: 900px;
  }
  &__input {
    margin-top: 16px;
    &:first-child {
      margin-top: 0;
    }
  }
  &__title {
    @extend %tg-news-card-title;
    margin-bottom: 12px;
  }
  &__button {
    margin-top: 6px;
    width: 100%;
  }
}

.news-holder {
  display: flex;
  flex-direction: column;
  max-width: 1000px;
  width: 100%;
  max-height: 600px;
  overflow: auto;
  gap: 12px 0;
  @include scrollbar;
  &::v-deep .card {
    box-shadow: none;
  }
}

.preview-section {
  margin-top: 40px;
  padding-top: 40px;
  border-top: 1px solid #ddd;
}

.preview-content {
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 8px;
  background: white;
}
</style>
