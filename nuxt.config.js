import news from './static/dynamic/news/news.json'
import specialties from './static/dynamic/specs/specs.json'
export default {
  ssr: false,
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'КИТЭК | Колледж инновационных технологий, экономики и коммерции',
    meta: [
      { charset: 'utf-8' },
      {
        name: 'viewport',
        content: 'width=device-width, initial-scale=1',
      },
      {
        hid: 'description',
        name: 'description',
        content:
          'Колледж инновационных технологий, экономики и коммерции в Омске – ведущее образовательное учреждение для поступления после 9 класса. Мы готовим специалистов в IT, поварском и кондитерском деле, гостиничном сервисе, бухгалтерии, юриспруденции, товароведении и судомеханике. Гарантируем качественное образование, востребованные профессии и поддержку в трудоустройстве для выпускников.',
      },
      {
        name: 'format-detection',
        content: 'telephone=no',
      },
      {
        hid: 'title',
        name: 'title',
        content: 'КИТЭК | Колледж инновационных технологий, экономики и коммерции',
      },
      {
        name: 'yandex-verification',
        content: 'bd6bb0dd5b55c163',
      },
      {
        hid: 'og:type',
        name: 'og:type',
        content: 'website',
      },
      {
        hid: 'og:url',
        name: 'og:url',
        content: 'https://omsktec.ru/',
      },
      {
        hid: 'og:title',
        name: 'og:title',
        content: 'КИТЭК | Колледж инновационных технологий, экономики и коммерции',
      },
      {
        hid: 'og:description',
        name: 'og:description',
        content: '',
      },
      {
        hid: 'og:image',
        name: 'og:image',
        content: '/icon.png',
      },

      {
        hid: 'apple-mobile-web-app-status-bar-style',
        name: 'apple-mobile-web-app-status-bar-style',
        content: 'default',
      },
      { hid: 'apple-mobile-web-app-capable', name: 'apple-mobile-web-app-capable', content: 'yes' },
      { hid: 'apple-mobile-web-app-title', name: 'apple-mobile-web-app-title', content: 'КИТЭК' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
      {
        rel: 'preconnect',
        href: 'https://fonts.gstatic.com',
        crossorigin: true,
      },
      {
        href: 'https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap',
        rel: 'stylesheet',
      },
      {
        href: 'https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;400;500;600;700;800;900&display=swap',
        rel: 'stylesheet',
      },
    ],
  },

  generate: {
    routes() {
      const nn = news.map((n) => `/news/${n.id}`)
      const ss = specialties.map((s) => `/specialties/${s.code}`)
      return [...nn, ...ss]
      // return [...ss]
    },
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['~assets/reset', '~assets/general', '~assets/common'],

  // * https://www.npmjs.com/package/@nuxtjs/style-resources
  // Глобальный импорт стилей | extend, vars, includes ...
  styleResources: {
    scss: ['./assets/constants.scss', './assets/tg.scss', './assets/block.scss'],
  },

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: ['plugins/vue-swiper', 'plugins/v-safe-html', 'plugins/v-scroll'],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: ['@nuxtjs/style-resources'],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    'nuxt-leaflet',

    // https://metrika.yandex.ru/dashboard?id=88299711
    [
      '@nuxtjs/yandex-metrika',
      {
        id: '88299711',
        clickmap: true,
        trackLinks: true,
        accurateTrackBounce: true,
        webvisor: true,
      },
    ],
    '@nuxtjs/robots',
  ],

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    icon: {
      fileName: '/favicon.ico',
    },
    manifest: {
      name: 'Приложение сайта колледжа "КИТЭК"',
      short_name: 'КИТЭК',
      lang: 'ru',
      display: 'standalone',
      theme_color: '#f9f9f9',
      background_color: '#f9f9f9',
      version_code: 1.9,
      icons: [
        {
          src: '/icons/16.png',
          sizes: '16x16',
        },
        {
          src: '/icons/20.png',
          sizes: '20x20',
        },
        {
          src: '/icons/29.png',
          sizes: '29x29',
        },
        {
          src: '/icons/32.png',
          sizes: '32x32',
        },
        {
          src: '/icons/40.png',
          sizes: '40x40',
        },
        {
          src: '/icons/50.png',
          sizes: '50x50',
        },
        {
          src: '/icons/57.png',
          sizes: '57x57',
        },
        {
          src: '/icons/58.png',
          sizes: '58x58',
        },
        {
          src: '/icons/60.png',
          sizes: '60x60',
        },
        {
          src: '/icons/64.png',
          sizes: '64x64',
        },
        {
          src: '/icons/72.png',
          sizes: '72x72',
        },
        {
          src: '/icons/76.png',
          sizes: '76x76',
        },
        {
          src: '/icons/80.png',
          sizes: '80x80',
        },
        {
          src: '/icons/87.png',
          sizes: '87x87',
        },
        {
          src: '/icons/100.png',
          sizes: '100x100',
        },
        {
          src: '/icons/114.png',
          sizes: '114x114',
        },
        {
          src: '/icons/120.png',
          sizes: '120x120',
        },
        {
          src: '/icons/128.png',
          sizes: '128x128',
        },
        {
          src: '/icons/144.png',
          sizes: '144x144',
        },
        {
          src: '/icons/152.png',
          sizes: '152x152',
        },
        {
          src: '/icons/167.png',
          sizes: '167x167',
        },
        {
          src: '/icons/180.png',
          sizes: '180x180',
        },
        {
          src: '/icons/192.png',
          sizes: '192x192',
        },
        {
          src: '/icons/maskable.png',
          sizes: '192x192',
          type: 'image/png',
          purpose: 'any maskable',
        },
        {
          src: '/icons/256.png',
          sizes: '256x256',
        },
        {
          src: '/icons/512.png',
          sizes: '512x512',
        },
        {
          src: '/icons/1024.png',
          sizes: '1024x1024',
        },
      ],
    },
    workbox: {
      runtimeCaching: [
        {
          urlPattern: 'https://fonts.googleapis.com/.*',
          handler: 'cacheFirst',
          method: 'GET',
          strategyOptions: { cacheableResponse: { statuses: [0, 200] } },
        },
        {
          urlPattern: 'https://fonts.gstatic.com/.*',
          handler: 'cacheFirst',
          method: 'GET',
          strategyOptions: { cacheableResponse: { statuses: [0, 200] } },
        },
        {
          urlPattern: 'https://omsktec.ru/dynamic/*/.*',
          handler: 'networkFirst',
        },
        {
          urlPattern: 'https://omsktec.ru/dynamic/news/events.json',
          handler: 'networkFirst',
        },
        {
          urlPattern: 'https://omsktec.ru/dynamic/news/.*',
          handler: 'networkFirst',
        },
        {
          urlPattern: 'https://omsktec.ru/documents/*.json',
          handler: 'networkFirst',
        },
      ],
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    // Позволяет считывать html файлы by import
    extend(config, ctx) {
      config.module.rules.push({
        test: /\.html$/i,
        use: [
          {
            loader: 'raw-loader',
          },
        ],
      })
    },
  },

  target: 'static',
  router: {
    // scrollBehavior(to, from, savedPosition) {
    //   return { x: 0, y: 0 }
    // },
    middleware: ['specialties-get'],
  },
}
