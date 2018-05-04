<template>
<div class="root">
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 查询</el-breadcrumb-item>
                <el-breadcrumb-item>基础查询</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="handle-box">
            <el-button class="handle-del mr10">批量下载</el-button>
            <el-select v-model="select_cate" placeholder="筛选来源" class="handle-select mr10">
                <el-option key="1" label="鼓楼医院" value="1"></el-option>
                <el-option key="2" label="其他" value="2"></el-option>
            </el-select>
            <el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>
            <el-button type="primary" icon="search">搜索</el-button>
        </div>
        <el-table :data="tableData" border style="width: 100%" ref="multipleTable" @selection-change="handleSelectionChange">
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column prop="registerDate" label="注册日期" sortable width="150">
            </el-table-column>
            <el-table-column prop="name" label="姓名" width="100">
            </el-table-column>
            <el-table-column prop="age" label="年龄" width="80">
            </el-table-column>
            <el-table-column prop="gender" label="性别" width="80">
            </el-table-column>
            <el-table-column prop="tel" label="联系方式" width="130">
            </el-table-column>
            <el-table-column prop="address" label="地址" :formatter="formatter">
            </el-table-column>
            <el-table-column label="操作" width="180">
                <template scope="scope">
                    <el-button size="small"
                            @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                    <el-button size="small" type="success"
                            @click="handleDetail(scope.$index, scope.row)">详情</el-button>
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
</div>
</template>

<script>
    export default {
        data() {
            return {
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
                let self = this;
                if(process.env.NODE_ENV === 'development'){
                    // self.url = '/ms/table/list';
                    self.url = '/api/users/getUsers';
                };
                self.$axios.get(self.url).then((res) => {
                    self.total = res.data.length + 1;
                    res.data = self.handleDate(res.data, self.cur_page);
                    self.tableData = res.data;
                })
            },
            handleDate(data, page) {
                var start = (page - 1) * 10;
                var end = Math.min(page * 10, data.length);
                var _data = [];
                for(let i = start; i < end; i++) {
                    data[i].registerDate = data[i].registerDate.substring(0, 10);
                    _data.push(data[i]);
                }
                return _data;
            },
            formatter(row, column) {
                return row.address;
            },
            filterTag(value, row) {
                return row.tag === value;
            },
            handleEdit(index, row) {
                this.$message('编辑第'+(index+1)+'行');
            },
            handleDetail(index, row) {
                this.$router.push({path: '/vuetable'});
            },
            handleSelectionChange: function(val) {
                this.multipleSelection = val;
            }
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
</style>