def handleRawQuery(queryset):
    order_dict = dict()
    order_list = []
    for i in queryset:
        print("id",i.id)
        if i.id not in order_dict:
            order_dict[i.id] = {
                "blog" :{
                    'id' : i.id,
                    'title' : i.title ,
                    'content' : i.content,
                    'user_id_id' : i.user_id_id ,
                    'date_created' : i.date_create,
                    'number_heart' : i.number_heart,
                    'number_comment' : i.number_comment,
                    'status_heart' : i.status_heart if i.status_heart != None else False
                },
                "img": i.file_img_blog,
                "comments" : [
                    {
                        "id" : i.comment_id,
                        'content' : i.comment_content,
                        'date_create' : i.comment_date_create,
                        'level' : i.comment_level ,
                        'user_id' : i.comment_user_id,
                        'number_heart' : i.comment_number_heart,
                        'user_profile' : i.comment_user_profile,
                        'parent_id' : i.parent,
                        'user_email' : i.comment_user_email,
                        'count_comment_child' : i.count_comment_child,
                        'status_heart_comment' : i.status_heart_comment if i.status_heart_comment != None else False,
                        'comment_is_edit' : i.comment_is_edit,
                        'file_media_comment' : i.file_media_comment
                    }
                ]
            }
        else :
            order_dict[i.id]["comments"].append({
                        "id" : i.comment_id,
                        'content' : i.comment_content,
                        'date_create' : i.comment_date_create,
                        'level' : i.comment_level ,
                        'user_id' : i.comment_user_id,
                        'number_heart' : i.comment_number_heart,
                        'user_profile' : i.comment_user_profile,
                        'parent_id' : i.parent,
                        'user_email' : i.comment_user_email,
                        'count_comment_child' : i.count_comment_child,
                        'status_heart_comment' : i.status_heart_comment if i.status_heart_comment != None else False,
                        'comment_is_edit' : i.comment_is_edit,
                        'file_media_comment' : i.file_media_comment
            })
    for i in order_dict:
        order_list.append(order_dict[i])
    return order_list

