<template>
  <div class="layout">
    <AppHeader />
    <div class="layout__nuxt">
      <Nuxt />
      <AppFooter />
    </div>
  </div>
</template>

<script>
export default {
  head() {
    return {
      meta: [
        {
          hid: 'og:title',
          property: 'og:title',
          content: 'КИТЭК | Колледж инновационных технологий, экономики и коммерции',
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content: 'Сайт образовательной организации',
        },
      ],
    }
  },
  beforeMount() {
    this.clearCache()
  },
  methods: {
    async clearCache() {
      const workbox = await window.$workbox
      if (workbox) {
        workbox.addEventListener('installed', (event) => {
          if (event.isUpdate) {
            window.location.reload()
          }
        })
        workbox.addEventListener('activate', function (event) {
          event.waitUntil(
            caches.keys().then(function (cacheNames) {
              return Promise.all(
                cacheNames
                  .filter(function (cacheName) {})
                  .map(function (cacheName) {
                    return caches.delete(cacheName)
                  })
              )
            })
          )
        })
      }
    },
  },
  watch: {
    route() {
      this.clearCache()
    },
  },
}
</script>

<style lang="scss">
body {
  @include scrollbar;
}
</style>

<style scoped lang="scss">
.layout {
  // padding: calc(118px + env(safe-area-inset-top, 44px)) 0 env(safe-area-inset-top, 34px) 0;
  @include small-media {
    overflow: hidden;
  }
  @include scrollbar;
}
</style>
