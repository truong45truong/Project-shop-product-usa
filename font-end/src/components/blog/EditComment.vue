<template>
    <div class="d-flex align-items-center d-flex edit-cmt-layout p-1" id="edit-comment-blog">
            <div class="col-sm-3 d-flex align-items-center mb-2">
                <p class="text-white m-0 ms-3"><b><i> Nhập nội dung chỉnh sửa : </i></b></p>
            </div>
            <input type="text" v-model="contentEdit" class="col-sm w-100 text-input-comment mb-2">
            <button class="button-6 col-sm-2 ms-2 mb-2" @click="editComment">
                Chỉnh sửa
            </button>
            <button class="d-block btn-cancel " @click="hide">
                Hủy
            </button>
    </div>
</template>
<script>
import { mapActions,mapGetters } from 'vuex'
import {CommentAction} from './../../common/comment.service'
export default {
    name: 'EditComment',
    props: {
        msg:''
    },
    data() {
        return {
            isAuthentication : false,
            contentEdit : '',
            comment_id : '',
        } 
    }
    ,
    created() {
        
            
    },
    
    computed: {
        ...mapGetters('auth', {
			get_user         : 'currentUser',
		}),
    },
    methods : {
        hide(){
            this.$emit('hide')
        },
        initValue(comment_id,content){
            this.comment_id = comment_id
            this.contentEdit = content
        },
        async editComment(){
            await CommentAction.actionEditComment({
                params : {
                    comment_id : this.comment_id,
                    content_comment : this.contentEdit
                }
            }).then(response => {
                console.log("eddit cmmt", response)
                this.$emit('upload',this.comment_id,this.contentEdit,response.edit_time)
                this.hide()
            })
        }

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.layout-expand-cmt {
    width:fit-content;
    height:fit-content;
    background-color: rgba(100, 100, 100, 0.6);
}
.btn-hide {
    cursor:pointer;

}
.btn-option-expand {
    cursor:pointer;
    font-size: 15px;
}
.btn-option-expand:hover {
    text-decoration: underline;
}

/* CSS */
.button-6 {
  align-items: center;
  background-color: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: .25rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: rgba(0, 0, 0, 0.85);
  cursor: pointer;
  display: inline-flex;
  font-family: system-ui,-apple-system,system-ui,"Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size: 16px;
  font-weight: 600;
  justify-content: center;
  line-height: 1.25;
  margin: 0;
  min-height: 3rem;
  padding: calc(.875rem - 1px) calc(1.5rem - 1px);
  position: relative;
  text-decoration: none;
  transition: all 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  width: auto;
}

.button-6:hover,
.button-6:focus {
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
  color: rgba(0, 0, 0, 0.65);
}

.button-6:hover {
  transform: translateY(-1px);
}

.button-6:active {
  background-color: #F0F0F1;
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
  color: rgba(0, 0, 0, 0.65);
  transform: translateY(0);
}
.edit-cmt-layout{
    border : 2px solid white;
}
.btn-cancel {
    background-color:transparent;
    border:none;
    text-decoration: underline;
    color:white;
}
</style>