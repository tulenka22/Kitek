<template>
  <block-ab title="Аттестация">
    <SplitLinks :links="links" />
  </block-ab>
</template>

<script>
import { createLink } from '~/core/helpers/link'
export default {
  data() {
    return {
      links: [
        createLink('http://obr55.ru/apr/', 'РИАЦ. Аттестация педагогических работников'),
        createLink(
          'https://mobr.omskportal.ru/oiv/mobr/otrasl/kpolitika/attestazia',
          'Списки аттестованных педагогических работников'
        ),
        createLink(
          'http://obr55.ru/wp-content/uploads/2022/01/Электронная-подача-документов_ФПГУ_1.pdf', 
          'Получение услуги «Аттестация педагогических работников» через платформу государственных сервисов ГОСУСЛУГИ (федеральный портал)'
        ),
      ],
    }
  },
}
</script>

<style scoped lang="scss"></style>
