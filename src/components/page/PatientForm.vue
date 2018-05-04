<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-date"></i> 表单</el-breadcrumb-item>
                <el-breadcrumb-item>基本表单</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="form-box">
            <el-form ref="form" :model="form" label-width="80px">
                <el-form-item label="病人姓名">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="年龄">
                    <el-input v-model="form.id"></el-input>
                </el-form-item>
                <el-form-item label="性别">
                    <el-select v-model="form.gender" placeholder="请选择">
                        <el-option key="male" label="男" value="male"></el-option>
                        <el-option key="female" label="女" value="female"></el-option>
                        <el-option key="unknown" label="未知" value="unknown"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="登记日期">
                    <el-col :span="12">
                        <el-date-picker type="date" placeholder="选择日期" v-model="form.date" style="width: 100%;"></el-date-picker>
                    </el-col>
                </el-form-item>
                <el-form-item label="联系方式">
                    <el-input v-model="form.tel"></el-input>
                </el-form-item>
                <el-form-item label="家庭住址">
                    <el-input v-model="form.address"></el-input>
                </el-form-item>
                <el-form-item label="就诊来源">
                    <el-input v-model="form.department"></el-input>
                </el-form-item>
                <el-form-item label="图像类别">
                    <el-radio-group v-model="form.type">
                        <el-radio label="文件"></el-radio>
                        <el-radio label="文件夹"></el-radio>
                        <el-radio label="链接"></el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="上传">
                    <input type="file" class="uploadFiles" multiple data-clear-btn="true" data-mini="true" v-show="form.type==='文件'"></input>
                    <input type="file" class="uploadFloder" multiple webkitdirectory data-clear-btn="true" data-mini="true" v-show="form.type==='文件夹'"></input>
                    <input type="url" class="uploadUrl" data-clear-btn="true" data-mini="true" v-show="form.type==='链接'"></input>
                </el-form-item>
                <el-form-item label="备注">
                    <el-input type="textarea" v-model="form.desc"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">提交</el-button>
                    <el-button>取消</el-button>
                </el-form-item>
            </el-form>
        </div>

    </div>
</template>

<script>
    export default {
        data: function(){
            return {
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: true,
                    type: '文件',
                    desc: ''
                }
            }
        },
        methods: {
            onSubmit() {
                this.$message.success('提交成功！');
            }
        }
    }
</script>