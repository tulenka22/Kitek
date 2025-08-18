<template>
  <p v-if="!documentsObj">{{ error }}</p>
  <ul v-else class="ab__list">
    <p class="ab__p" v-safe-html="documentsObj.title" />
    <li class="ab__link" v-for="(doc, docidx) of documentsObj.docs" :key="docidx">
      <a target="_blank" class="ab__inline-link" :href="doc.url">
        <icon-wrapper class="ab__icon" width="24" height="32">
          <icon-document />
        </icon-wrapper>
        {{ doc.name }}
      </a>
    </li>
  </ul>
</template>

<style lang="scss" scoped>
.ab {
  &__link {
    margin-left: 0;
    &::before {
      width: 0;
      margin-left: 0;
    }
  }
  &__inline-link {
    display: flex;
    align-items: center;
  }
  &__icon {
    margin-right: 6px;
    color: $accent-color;
  }
}
</style>

<script>
import { loadDynamic } from '~/core/helpers/file'
export default {
  name: 'CommonDocumentsList',
  props: {
    jsonPath: {
      type: String,
    },
  },
  data() {
    return {
      documentsObj: null,
      title: 'Загрузка...',
      error: 'Загрузка...',
    }
  },
  async created() {
    try {
      this.documentsObj = JSON.parse(await loadDynamic(this.jsonPath))
      this.title = this.documentsObj.title
    } catch {
      this.error = `Ошибка при загрузке документа '${this.jsonPath}'`
    }
  },
}
</script>
