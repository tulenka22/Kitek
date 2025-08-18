<template>
  <Navdrop :columns="columns" grid="1" />
</template>

<script>
import { createLink, createColumn } from '~/core/helpers/link'
export default {
  name: 'NavdropTeacher',
  data() {
    return {
      columns: [
        createColumn(
          '',
          createLink('/teacher/certificate', 'Аттестация'),
          createLink('/teacher/training', 'Повышение квалификации'),
          createLink('/teacher/contests', 'Конкурсы'),
          createLink('/teacher/useful-links', 'Полезные ссылки')
        ),
      ],
    }
  },
}
</script>
