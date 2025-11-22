<template>
  <Navdrop :columns="columns" grid="2" />
</template>

<script>
import { createLink, createColumn } from '~/core/helpers/link'
export default {
  name: 'NavdropProjects',
  data() {
    return {
      columns: [
        createColumn(
          '',
          createLink(
            '/projects/promotion',
            'Федеральный проект «Содействие занятости» Национального проекта «Демография»'
          ),
          createLink('/projects/demo-ekzam', 'Демонстрационный экзамен'),
          createLink('/projects/ticket', 'Билет в будущее'),
          createLink('/projects/inko', 'РИП-ИнКО')
        ),
        createColumn(
          '',
          
          createLink('/projects/workshop', 'Мастерские'),
          createLink('/projects/soo', 'Внедрение стандарта среднего общего образования'),
          createLink('/professional', 'ФП «Профессионалитет»'),
          createLink('/projects/predp', 'Учебно-производственный комплекс')
        ),
      ],
    }
  },
}
</script>
