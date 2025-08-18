<template>
  <div class="links">
    <AppBlock title="Полезные ссылки">
      <template #content>
        <SplitLinks :links="links" :gos="true" :support="true" />
      </template>
    </AppBlock>
  </div>
</template>

<script>
import { links } from '~/core/lists'
export default {
  name: 'BlockLinks',
  data() {
    return {
      links,
    }
  },
}
</script>

<style scoped lang="scss">
.links {
  margin-top: 60px;
  &__group {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
  }
  &__icon {
    width: 300px;
    height: 180px;
    object-fit: contain;
    margin-right: 16px;
    @include medium-media {
      width: 180px;
      height: 120px;
    }
  }

  &__img {
    width: 1084px;
    height: 222px;
    margin: 0 auto;
    margin-top: 48px;
  }
}
</style>
