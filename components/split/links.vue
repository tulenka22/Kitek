<template>
  <main class="links__content">
    <div class="links__grid">
      <a
        target="_blank"
        v-for="(link, idx) of links"
        :key="idx"
        :href="link.url"
        rel="nofollow"
        class="links__btn"
        >{{ link.title }}</a
      >
    </div>
    <block-gos v-if="gos" />
    <block-support v-if="support" />
  </main>
</template>

<script>
export default {
  name: 'SplitLinks',
  props: {
    links: {
      type: Array,
      default() {
        return []
      },
    },
    gos: {
      type: Boolean,
      default: false,
    },
    support: {
      type: Boolean,
      default: false,
    },
  },
}
</script>

<style scoped lang="scss">
.links {
  &__content {
    padding: 16px 32px;
    @include medium-media {
      padding: 24px 0;
    }
  }
  &__grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
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
  &__gos {
    width: 100%;
    height: 315px;
  }
}
</style>
