<template>
  <block-ab title="Конкурсы">
    <SplitLinks :links="links" />
  </block-ab>
</template>

<script>
import { createLink } from '~/core/helpers/link'
export default {
  data() {
    return {
      links: [
        createLink(
          'https://irooo.ru/nauchno-metodicheskoe-obespechenie/nepreryvnoe-professionalnoe-razvitie-pedagogov-omskoj-oblasti-v-t-ch-molodykh-pedagogov/konkursy-professionalnogo-masterstva',
          'Конкурсы профессионального мастерства'
        ),
        createLink(
          'http://проф-обр.рф/news/2023-01-22-2462',
          'Всероссийский конкурсно-образовательный марафон «Наставник- мастер своего дела» '
        ),
        createLink(
          'http://проф-обр.рф/news/2021-09-01-313',
          'Всероссийский педагогический конкурс «Лучшие практики среднего профессионального образования»'
        ),
        createLink(
          'http://проф-обр.рф/news/2021-05-01-151',
          'XV- Всероссийская интернет – конференция «Поиск эффективных форм и методов обучения в профессиональном образовании»'
        ),
      ],
    }
  },
}
</script>

<style scoped lang="scss"></style>
