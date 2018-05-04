<template>
<div class="root">
    <div class="table" v-if="is_superuser">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 后台管理</el-breadcrumb-item>
                <el-breadcrumb-item>权限控制</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="handle-box">
            <el-select v-model="select_cate" placeholder="用户类型" class="handle-select mr10">
                <el-option key="1" label="激活用户" value="1"></el-option>
                <el-option key="2" label="未激活用户" value="2"></el-option>
            </el-select>
            <el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>
            <el-button type="primary" icon="search">搜索</el-button>
        </div>
        <el-table :data="tableData" border style="width: 100%" ref="multipleTable" @selection-change="handleSelectionChange">
            <el-table-column prop="username" label="用户名" width="90">
            </el-table-column>
            <el-table-column prop="email" label="邮箱地址" width="180">
            </el-table-column>
            <el-table-column prop="password" label="密码" width="90">
            </el-table-column>
            <el-table-column prop="add" label="add" width="80">
                <template scope="scope">
                    <el-checkbox label=""></el-checkbox>
                </template>
            </el-table-column>
            <el-table-column prop="edit" label="edit" width="80">
                <template scope="scope">
                    <el-checkbox label=""></el-checkbox>
                </template>
            </el-table-column>
            <el-table-column prop="query" label="query" width="80">
                <template scope="scope">
                    <el-checkbox label=""></el-checkbox>
                </template>
            </el-table-column>
            <el-table-column prop="delete" label="delete" width="80">
                <template scope="scope">
                    <el-checkbox label=""></el-checkbox>
                </template>
            </el-table-column>
            <el-table-column prop="status" label="状态" width="90">
            </el-table-column>
            <el-table-column label="操作" width="180">
                <template scope="scope">
                    <el-button size="small"
                            @click="handleEdit(scope.$index, scope.row)">确认</el-button>
                    <el-button size="small" type="success"
                            @click="handleDel(scope.$index, scope.row)">删除用户</el-button>
                </template>
            </el-table-column>
        </el-table>
        <div class="pagination">
            <el-pagination
                    @current-change="handleCurrentChange"
                    :current-page="currentPage"
                    :page-size="10"
                    layout="prev, pager, next"
                    :total="total">
            </el-pagination>
        </div>
    </div>
    <div class="tips" v-else="is_superuser">You hava no permission to do this action！</div>
</div>
</template>

<script>
    export default {
        data() {
            return {
                is_superuser: true,
                url: '../../../static/vuetable.json',
                tableData: [],
                cur_page: 1,
                multipleSelection: [],
                select_cate: '',
                select_word: '',
                total: 0,
                currentPage: 1
            }
        },
        created(){
            this.getData();
        },
        methods: {
            handleCurrentChange(val){
                this.cur_page = val;
                this.getData();
            },
            getData(){
                var data = [{
                    username: '张三',
                    email: 'zhangsan@163.com',
                    password: '******',
                    add: true,
                    edit: false,
                    query: true,
                    delete: false,
                    status: '未激活'
                },{
                    username: '李四',
                    email: '12345678@qq.com',
                    password: '******',
                    add: true,
                    edit: false,
                    query: true,
                    delete: false,
                    status: '未激活'
                },{
                    username: '王二',
                    email: 'zhangsan@163.com',
                    password: '******',
                    add: true,
                    edit: false,
                    query: true,
                    delete: false,
                    status: '未激活'
                },{
                    username: 'zhaojun',
                    email: '1274802683@qq.com',
                    password: '******',
                    add: true,
                    edit: false,
                    query: true,
                    delete: false,
                    status: '激活'
                }];
                this.tableData = data;
            },
            filterTag(value, row) {
                return row.tag === value;
            },
            handleEdit(index, row) {
                this.$message('确认并提交修改');
            },
            handleDel(index, row) {
                this.$message('删除该用户！');
            },
            handleSelectionChange() {}
        }
    }
</script>

<style scoped>
.handle-box{
    margin-bottom: 20px;
}
.handle-del{
    border-color: #bfcbd9;
    color: #999;
}
.handle-select{
    width: 120px;
}
.handle-input{
    width: 300px;
    display: inline-block;
}
.tips{
    font-size: 20px;
}
</style>