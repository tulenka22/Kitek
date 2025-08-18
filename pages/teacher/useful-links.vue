<template>
  <block-ab title="Полезные ссылки">
    <SplitLinks :links="links" :gos="true" />
  </block-ab>
</template>

<script>
import { links } from '~/core/lists'
export default {
  data() {
    return {
      links,
    }
  },
}
</script>

<style scoped lang="scss">
.ab {
  &__grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 24px;
  }
  &__btn {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 12px;
    border-radius: 5px;
    background-color: $primary-color;
    color: $bg-primary;
    text-align: center;
    @include tg(18px, 700, 18px);
  }
  &__img {
    width: 1084px;
    height: 222px;
    margin: 0 auto;
    margin-top: 48px;
  }
}
</style>
