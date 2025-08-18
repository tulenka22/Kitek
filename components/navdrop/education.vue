<template>
  <Navdrop :columns="columns" style="display: none" />
</template>

<script>
import { createLink, createColumn } from '~/core/helpers/link'
export default {
  name: 'NavdropEducation',
  data() {
    return {
      columns: [
        createColumn(
          '',
          createLink('/education', ''),
          createLink('/education', ''),
          createLink('/education', '')
        ),
      ],
    }
  },
}
</script>
