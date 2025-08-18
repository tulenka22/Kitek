<template>
  <div class="elem elem__grid" :class="`elem__grid-${grid}`">
    <div
      class="column column__grid"
      :class="`elem__grid-${grid}`"
      v-for="(col, idx) of columns"
      :key="idx">
      <h3 v-if="col.title" class="column__title">{{ col.title }}</h3>
      <nuxt-link
        :to="link.url"
        class="column__link"
        active-class="column__link-active"
        v-for="(link, linkIdx) of col.links"
        :key="linkIdx"
        exact>
        {{ link.title }}
      </nuxt-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navdrop',
  props: {
    columns: {
      type: Array,
      default() {
        return []
      },
    },
    grid: {
      type: String,
      default: '3',
    },
  },
}
</script>

<style scoped lang="scss">
@import './helpers/scss';
</style>
