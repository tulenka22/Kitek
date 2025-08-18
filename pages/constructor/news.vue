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
          <common-textarea
            v-model="selectedOrNew.description"
            rows="8"
            label="Описание"
            class="form__input" />
          <div class="form__group" v-if="!isSelectedCard">
            <common-button class="form__button" @click="addNew">Добавить</common-button>
            <common-button class="form__button" @click="cleanForm">Очистить</common-button>
          </div>
          <div class="form__group" v-else>
            <common-button class="form__button" @click="saveCurrent">Сохранить</common-button>
            <common-button class="form__button" @click="deleteCurrent">Удалить</common-button>
            <common-button class="form__button" @click="goBack">Назад</common-button>
          </div>
          <common-button class="form__button" @click="copyAll">
            Скопировать код всех новостей
          </common-button>
          <div class="news-holder">
            <h2 class="form__title" style="margin-top: 12px">Предпросмотр</h2>
            <entities-new-card
              @click.native.stop.prevent="selectNews(n)"
              :instance="selectedOrNew" />
          </div>
        </div>
      </div>
    </div>
    <div class="markdown">
      <common-textarea rows="80" v-model="markdown" />
      <div class="markdown__content" v-safe-html="markdownParsed" />
    </div>
    <common-button @click="copyPage"> Скопировать страницу </common-button>
  </block-ab>
</template>

<script>
// Todo: Save as file
import { loadDynamic } from '~/core/helpers/file'
import Markdown from '@nuxt/markdown'
export default {
  async created() {
    this.mdParser = new Markdown({ toc: false, sanitize: false })

    try {
      this.news = JSON.parse(await loadDynamic('dynamic/news/news.json'))
    } catch {
      console.error('Проверьте валидность JSON новостей и событий!')
    }
  },
  data() {
    return {
      selectedOrNew: {
        id: Date.now(),
        title: 'Заголовок',
        description: 'Описание новости',
      },
      news: [],
      markdown: '',
      markdownParsed: '',
      mdParser: null,
    }
  },
  computed: {
    isSelectedCard() {
      return this.news.some((n) => this.selectedOrNew.id === n.id)
    },
  },
  watch: {
    async markdown(newVal) {
      const content = await this.mdParser.toMarkup(newVal)
      this.markdownParsed = content.html
    },
  },
  methods: {
    selectNews(nCard) {
      this.selectedOrNew = { ...nCard }
    },
    addNew() {
      this.news.unshift({ ...this.selectedOrNew })
      this.cleanForm()
    },
    cleanForm() {
      this.selectedOrNew = {
        id: new Date(),
        title: 'Заголовок',
        description: 'Описание новости',
      }
    },
    saveCurrent() {
      const currentIndex = this.news.findIndex((n) => n.id === this.selectedOrNew.id)
      this.$set(this.news, currentIndex, { ...this.selectedOrNew })
    },
    deleteCurrent() {
      this.news = this.news.filter((n) => n.id !== this.selectedOrNew.id)
    },
    goBack() {
      this.cleanForm()
    },
    copyAll() {
      navigator.clipboard.writeText(JSON.stringify(this.news))
    },
    copyPage() {
      navigator.clipboard.writeText(this.markdownParsed)
    },
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

.markdown {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0 24px;
  margin-top: 24px;
  &__content {
    border: 1px solid #dddddd;
    padding: 12px;
  }
}
</style>
