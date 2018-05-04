<template>
    <div class="sidebar">
        <el-menu :default-active="onRoutes" class="el-menu-vertical-demo" unique-opened router>
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index">
                        <template slot="title"><i :class="item.icon"></i>{{ item.title }}</template>
                        <el-menu-item v-for="(subItem,i) in item.subs" :key="i" :index="subItem.index">{{ subItem.title }}
                        </el-menu-item>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index">
                        <i :class="item.icon"></i>{{ item.title }}
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                items: [
                    {
                        icon: 'el-icon-star-on',
                        index: 'readme',
                        title: '简介'
                    },
                    {
                        icon: 'el-icon-menu',
                        index: '2',
                        title: '查询',
                        subs: [
                            {
                                index: 'basetable',
                                title: '基础查询'
                            },
                            {
                                index: 'vuetable',
                                title: '图像查询'
                            }
                        ]
                    },
                    {
                        icon: 'el-icon-upload2',
                        index: '3',
                        title: '病例上传',
                        subs: [
                            // {
                            //     index: 'baseform',
                            //     title: '病例填写'
                            // },
                            {
                                index: 'patientform',
                                title: '病例填写'
                            },
                            {
                                index: 'vueeditor',
                                title: '编辑器'
                            },
                            {
                                index: 'markdown',
                                title: 'markdown'
                            },
                            {
                                index: 'upload',
                                title: '文件上传'
                            }
                        ]
                    },
                    {
                        icon: 'el-icon-date',
                        index: 'drag',
                        title: '图像管理'
                    },
                    {
                        icon: 'el-icon-setting',
                        index: 'basecharts',
                        title: '后台管理'
                    }
                    // {
                    //     icon: 'el-icon-date',
                    //     index: 'drag',
                    //     title: '拖拽'
                    // }
                ]
            }
        },
        computed:{
            onRoutes(){
                return this.$route.path.replace('/','');
            }
        }
    }
</script>

<style scoped>
    .sidebar{
        display: block;
        position: absolute;
        width: 250px;
        left: 0;
        top: 70px;
        bottom: 0;
        background: #2E363F;
    }
    .sidebar > ul {
        height: 100%;
    }
</style>
