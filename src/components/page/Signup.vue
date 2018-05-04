<template>
    <div class="login-wrap">
        <div class="ms-title">脑磁共振图像管理系统</div>
        <div class="ms-header">
            <a class="switch_btn" @click="goLogin">登录</a>
            <a class="switch_btn_active">注册</a>
        </div>
        <div class="ms-login">
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px" class="demo-ruleForm">
                <el-form-item prop="username">
                    <el-input v-model="ruleForm.username" placeholder="username"></el-input>
                </el-form-item>
                <el-form-item prop="email">
                    <el-input v-model="ruleForm.email" placeholder="email"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" placeholder="password" v-model="ruleForm.password" @keyup.enter.native="submitForm('ruleForm')"></el-input>
                </el-form-item>
                <div class="login-btn">
                    <el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
                </div>
                <p class="tips">Tips:点击「注册」按钮，即代表你同意<span style="color: #00d1b2">《保密协议》</span></p>
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
                    email: '',
                    password: ''
                },
                rules: {
                    username: [
                        { required: true, message: '请输入用户名', trigger: 'blur' }
                    ],
                    email: [
                        { required: true, message: '请输入邮箱地址', trigger: 'blur' }
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
            goLogin() {
                this.$router.push('/login');
            }
        }
    }
</script>

<style scoped>
    .login-wrap{
        position: relative;
        width: 100%;
        height: 100%;
    }
    .ms-title{
        position: absolute;
        top: 50%;
        width: 100%;
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
        left: 50%;
        top: 50%;
        width: 300px;
        height: 210px;
        margin: -120px 0 0 -190px;
        padding: 40px;
        border-radius: 5px;
        background: #fff;
    }
    .login-btn{
        text-align: center;
    }
    .login-btn button{
        width: 100%;
        height: 36px;
    }
    .tips{
        font-size: 12px;
        line-height: 30px;
        color: #999;
    }
</style>