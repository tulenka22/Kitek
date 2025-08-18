<template>
  <Navdrop :columns="columns" grid="1" />
</template>

<script>
import { createLink, createColumn } from '~/core/helpers/link'
export default {
  name: 'NavdropEnrolle',
  data() {
    return {
      columns: [
        createColumn(
          '',
          createLink('/specialties', 'Специальности и профессии'),
          createLink('/enrolle/committee', 'Приёмная комиссия'),
          createLink('/enrolle/rating', 'Рейтинг абитуриентов'),
          createLink('/enrolle/orders', 'Приказы о зачислении'),
          createLink('/enrolle/prof', 'Профориентационная работа')
        ),
      ],
    }
  },
}
</script>
