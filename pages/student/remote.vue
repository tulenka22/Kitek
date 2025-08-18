<template>
  <block-ab title="Дистанционное обучение">
    <SplitLinks :links="links" />
  </block-ab>
</template>

<script>
import { createLink } from '~/core/helpers/link'
export default {
  data() {
    return {
      links: [
        createLink('https://edu.omsktec.ru/', 'Образовательный портал БПОУ «КИТЭК»'),
        createLink('https://dnevnik.ru', 'Автоматизированная информационная система Дневник.ру'),
        createLink('https://book.ru', 'Электронная библиотечная система BOOK.ru'),
        createLink('https://sferum.ru/', 'Образовательная платформа «Сферум»'),
        createLink('https://vk.com/omsktec', 'Официальная страница БПОУ «КИТЭК» в VK'),
      ],
    }
  },
}
</script>

<style scoped lang="scss">
.link {
  text-decoration: underline;
  text-underline-offset: 2px;
  // margin-left: 2px;
}
</style>
