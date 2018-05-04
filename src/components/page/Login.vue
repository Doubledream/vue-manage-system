<template>
    <div class="login-wrap">
        <div class="ms-title">脑磁共振图像管理系统</div>
        <div class="ms-header">
            <a class="switch_btn_active">登录</a>
            <a class="switch_btn" @click="goSignup">注册</a>
        </div>
        <div class="ms-login">
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px" class="demo-ruleForm">
                <el-form-item prop="username">
                    <el-input v-model="ruleForm.username" placeholder="username"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" placeholder="password" v-model="ruleForm.password" @keyup.enter.native="submitForm('ruleForm')"></el-input>
                </el-form-item>
                <div class="login-btn">
                    <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
                </div>
                <a class="forget-psd">忘记密码？</a>
            </el-form>
        </div>
    </div>
</template>

<script>
    export default {
        data: function(){
            return {
                ruleForm: {
                    username: '',
                    password: ''
                },
                rules: {
                    username: [
                        { required: true, message: '请输入用户名', trigger: 'blur' }
                    ],
                    password: [
                        { required: true, message: '请输入密码', trigger: 'blur' }
                    ]
                }
            }
        },
        methods: {
            submitForm(formName) {
                const self = this;
                self.$refs[formName].validate((valid) => {
                    if (valid) {
                        localStorage.setItem('ms_username',self.ruleForm.username);
                        self.$router.push('/readme');
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            goSignup() {
                this.$router.push('/signup');
            }
        }
    }
</script>

<style scoped>
    .login-wrap{
        position: relative;
        width:100%;
        height:100%;
    }
    .ms-title{
        position: absolute;
        top:50%;
        width:100%;
        margin-top: -230px;
        text-align: center;
        font-size:30px;
        color: #fff;
    }
    .ms-header{
        position: absolute;
        display: flex;
        top: 50%;
        left: 50%;
        width: 200px;
        margin-top: -165px;
        margin-left: -100px;
        font-size: 20px;
        font-weight: bold;
        color: #ccc;
    }
    .ms-header a{
        flex: 1;
        width: 150px;
        padding-bottom: 10px;
        text-align: center;
        cursor: pointer;
    }
    .switch_btn_active{
        color: #fff;
        border-bottom: 2px solid #fff;
    }
    .ms-login{
        position: absolute;
        left:50%;
        top:50%;
        width:300px;
        height:160px;
        margin:-120px 0 0 -190px;
        padding:40px;
        border-radius: 5px;
        background: #fff;
    }
    .login-btn{
        text-align: center;
    }
    .login-btn button{
        width:100%;
        height:36px;
    }
    .forget-psd{
        margin-top: 5px;
        font-weight: bold;
        font-size: 14px;
        color: #999;
        float: right;
        line-height: 30px;
        cursor: pointer;
    }
    .forget-psd:hover{
        color: #00d1b2;
    }
</style>