from xlwt import Workbook
houduan = {
    "4000": {
        "zh": "请求失败",
        "en": "Request Failed",
        "hk": "請求失敗",
        "jp": "リクエストが失敗しました。"
    },
    "4010": {
        "zh": "请重新登录",
        "en": "Please sign in again",
        "hk": "請重新登錄",
        "jp": "もう一度サインインしてください"
    },
    "4011": {
        "zh": "密码错误",
        "en": "Incorrect password",
        "hk": "密碼錯誤",
        "jp": "パスワードが正しくありません"
    },
    "4012": {
        "zh": "请输入正确的用户名和密码",
        "en": "Please input the correct username and password.",
        "hk": "請輸入正確的使用者名和密碼",
        "jp": "もう一度ログインしてください"
    },
    "4013": {
        "zh": "用户已存在",
        "en": "User already exists",
        "hk": "用戶已存在",
        "jp": "このユーザーは既に存在しています。"
    },
    "4014": {
        "zh": "用户不存在",
        "en": "User does not exit",
        "hk": "用戶不存在",
        "jp": "ユーザが終了しない。"
    },
    "4015": {
        "zh": "使用权已到期，请联系管理员续期",
        "en": "The permission has expired, please contact the administrator to renew",
        "hk": "使用權已到期，請聯繫管理員續期",
        "jp": "管理者に連絡して更新してください。"
    },
    "4016": {
        "zh": "请输入正确的密码",
        "en": "Please input the correct password.",
        "hk": "請輸入正確的密碼",
        "jp": "正しいパスワードを入力してください。"
    },
    "4030": {
        "zh": "拒绝操作",
        "en": "Operation Denied",
        "hk": "拒絕操作",
        "jp": "操作拒否"
    },
    "4031": {
        "zh": "申请的端口已经分配，重新选择端口进行服务发布",
        "en": "Requested port allocated. Please reselect an port to publish your service.",
        "hk": "申請的端口已經分配，重新選擇進行服務發佈",
        "jp": "要求されたインタフェースが割り当てられました。サービスをリリースするインターフェースを再選択してください。"
    },
    "4032": {
        "zh": "发布的服务正在运行，请停止后再删除训练",
        "en": "The released service is still running, please delete after stopping it",
        "hk": "發布的服務正在運行，請停止後再刪除訓練",
        "jp": "リリースされたサービスがまだ稼働しているので、停止後に削除してください"
    },
    "4040": {
        "zh": "资源不存在",
        "en": "Resource non-existent.",
        "hk": "資源不存在",
        "jp": "リソースが存在しません。"
    },
    "4041": {
        "zh": "模型不存在",
        "en": "Model non-existent.",
        "hk": "模型不存在",
        "jp": "モデルは存在しません。"
    },
    "4042": {
        "zh": "错误路径",
        "en": "Path Incorrect",
        "hk": "錯誤路徑",
        "jp": "ルートは間違っています。"
    },
    "4043": {
        "zh": "文件不存在",
        "en": "File non-existent.",
        "hk": "文件不存在",
        "jp": "ファイルが存在しません。"
    },
    "4044": {
        "zh": "文件已存在",
        "en": "File already exists.",
        "hk": "文件已存在",
        "jp": "ファイルが既に存在します。"
    },
    "4045": {
        "zh": "文件格式错误",
        "en": "File format incorrect.",
        "hk": "文件格式錯誤",
        "jp": "ファイルのフォーマットは間違っています。"
    },
    "4046": {
        "zh": "项目名称重复，请修改",
        "en": "Duplicate project name, please modify",
        "hk": "項目名稱重複，請修改",
        "jp": "プロジェクト名が重複しています。変更してください。"
    },
    "4047": {
        "zh": "标签类型已经存在，请重新命名",
        "en": "Label type already exists, please rename",
        "hk": "標籤類型已經存在，請重新命名",
        "jp": "ラベルタイプは既に存在しています。名前を変更してください。"
    },
    "4048": {
        "zh": "上传的标注数据和当前图片不一致，请确认后重新上传",
        "en": "The uploaded label data is inconsistent with the current image, please confirm and re-upload",
        "hk": "上傳的標註數據和當前圖片不一致，請確認後重新上傳",
        "jp": "アップロードされた注釈データが現在の画像と一致していません。確認して再アップロードしてください"
    },
    "4049": {
        "zh": "有部分图片没有对应的标注数据，请确认后重新上传",
        "en": "Some pictures do not have corresponding label data, please confirm and re-upload",
        "hk": "有部分圖片沒有對應的標註數據，請確認後重新上傳",
        "jp": "一部の写真には対応するラベルデータがありません。確認して再アップロードしてください"
    },
    "4050": {
        "zh": "禁止下载",
        "en": "Download not allowed.",
        "hk": "禁止下載",
        "jp": "ダンロード禁止です。"
    },
    "4051": {
        "zh": "请标注缺陷特征",
        "en": "Please mark defect features",
        "hk": "請標註缺陷特徵",
        "jp": "欠陥の特徴をマークしてください"
    },
    "4052": {
        "zh": "无法获取训练数据，训练开启失败",
        "en": "Unable to obtain training data, training failed to start",
        "hk": "無法獲取訓練數據，訓練開啟失敗",
        "jp": "トレーニングデータを取得できず、トレーニングを開始できませんでした"
    },
    "4053": {
        "zh": "未设置roi，请先设置roi",
        "en": "roi is not set, please set roi first",
        "hk": "未設置roi，請先設置roi",
        "jp": "roiが設定されていません。最初にroiを設定してください"
    },
    "4054": {
        "zh": "至少需要标注2张图片才能进行数据划分，请进行标注",
        "en": "At least 2 images need to be labeled for data split, please label",
        "hk": "至少需要標註2張圖片才能進行數據劃分，請進行標註",
        "jp": "データを分割するために、少なくとも2枚の画像にラベルが必要です。"
    },
    "4055": {
        "zh": "您输入的文本不支持识别，请重新输入",
        "en": "The text you entered is not recognized, please re-enter",
        "hk": "您輸入的文本不支持識別，請重新輸入",
        "jp": "入力したテキストが認識されません。再入力してください"
    },
    "4120": {
        "zh": "可用GPU数量不足",
        "en": "No enough available GPUs.",
        "hk": "可用GPU數量不足",
        "jp": "使用可能なGPUが足りないです。"
    },
    "4121": {
        "zh": "您所拥有的资源已耗尽，无法进行训练，请清理历史项目，或联系管理员进行扩容!",
        "en": "Unable to start training becuase resources are used up. Please remove past projects or contact admin for more resources.",
        "hk": "您所擁有的資源已耗盡，無法進行訓練，請清理歷史，或聯繫管理員",
        "jp": "リソースを使い切ってしまったため、トレーニングを開始することができません。過去のプロジェクトを削除するか、管理者に連絡してください。"
    },
    "4122": {
        "zh": "上传图像数量最多为2000，上传失败!",
        "en": "The maximum number of uploaded images is 2000, the upload failed!",
        "hk": "上傳圖像數量最多為2000，上傳失敗!",
        "jp": "アップロードされた画像の最大数は2000です、アップロードに失敗しました"
    },
    "4160": {
        "zh": "参数错误",
        "en": "Parameter Incorrect",
        "hk": "參數錯誤",
        "jp": "パラメータエラー"
    },
    "5000": {
        "zh": "内部服务器错误",
        "en": "Internal Server Error",
        "hk": "內部伺服器錯誤",
        "jp": "内部サーバーエラー"
    },
    "5001": {
        "zh": "上传失败",
        "en": "Upload Failed ",
        "hk": "上傳失敗",
        "jp": "アップロード失敗"
    },
    "5002": {
        "zh": "请上传zip格式压缩包",
        "en": "Please upload zip format compressed file",
        "hk": "請上傳zip格式壓縮包",
        "jp": "ZIP形式の圧縮ファイルをアップロードしてください。"
    },
    "5003": {
        "zh": "请上传正确格式图片（jpeg，png，tiff，bmp，jpg）",
        "en": "Please upload images with supported suffix(jpeg/png/tiff/bmp/jpg)",
        "hk": "請上傳正確格式圖片（jpeg，png，tiff，bmp，jpg）",
        "jp": "対応する拡張子の画像をアップロードしてください（jpeg/png/tiff/bmp/jpg）"
    },
    "5004": {
        "zh": "图片所属中没有测试集，请配置后重试",
        "en": "There is no test set in the image, please retry after configuration",
        "hk": "圖片所屬中沒有測試集，請配置後重試",
        "jp": "イメージにテストセットがありません。構成後に再試行してください"
    },
    "4003": {
        "zh": "当前模块训练已启动，请勿重复启动",
        "en": "The current module training has been started, please do not start it again",
        "hk": "當前模塊訓練已啟動，請勿重複啟動",
        "jp": "現在のモジュールトレーニングが開始されました。再度開始しないでください。"
    },
    "4004": {
        "zh": "当前模块推理已启动，请勿重复启动",
        "en": "The current module inference has been started, please do not start it again",
        "hk": "當前模塊推理已啟動，請勿重複啟動",
        "jp": "現在のモジュール推論が開始されました。再度開始しないでください"
    },
    "4005": {
        "zh": "当前方案中视图数量大于2000张，请删除图片后重试",
        "en": "Current solution has more than 2000 images, please delete the extra images and try again",
        "hk": "當前方案中視圖數量大於2000張，請刪除圖片後重試",
        "jp": "現在のプログラムの再生回数が2000回を超えています。画像を削除して、もう一度やり直してください。"
    },
    "4006": {
        "zh": "您上传的标注文件shape异常，请检查后重新进行上传",
        "en": "The shape of the label file you uploaded is abnormal, please check and re-upload",
        "hk": "您上傳的標註文件shape異常，請檢查後重新進行上傳",
        "jp": "アップロードしたアノテーションファイルの形状が異常ですので、確認して再アップロードしてください"
    },
    "4007": {
        "zh": "父模块 '%s' 正在训练或推理中,子模块输入会产生变化。请在其结束后在进行此操作",
        "hk": "父模塊 '%s' 正在訓練或推理中,子模塊輸入會產生變化。請在其結束後在進行此操作",
        "en": "Parent module '%s' is in training or inference, and child module input changes. Please wait until it's over",
        "jp": "親モジュール '%s'はトレーニング中または推論中であり、子モジュールの入力が変更されます。 終わるまでお待ちください"
    }
}

# for k,v in houduan.items():
#     print("kk,,vvv",k,v)
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')


zh = []
hk = []
en = []
jp = []

print(zh)
if isinstance(houduan, dict):
  count = 0
  for k in houduan.keys():
    cisu = 0
    if isinstance(houduan[k], dict):
        for i in houduan[k]:
            if isinstance(houduan[k][i], str):
              print(houduan[k], type(houduan[k]))

              for kk in houduan[k].keys():
                print("kkkkk", kk, type(kk))
                if cisu >= 4:
                  break
                if kk == "zh":
                  zh.append(houduan[k][i])  # 第二层的值
                  print("zh", houduan[k][kk])
                  print("houduan[kk][i])", houduan[k][i])
                  sheet1.write(count, 0, "{}".format(houduan[k][kk]))
                  cisu += 1
                # print(list)
                elif kk == "en":
                  en.append(houduan[k][i])  # 第二层的值
                  print("en", houduan[k][kk])
                  sheet1.write(count, 2, "{}".format(houduan[k][kk]))
                  cisu += 1
                elif kk == "hk":
                  hk.append(houduan[k][kk])  # 第二层的值
                  print("hkhkhkhouduan[kk][i])", houduan[k][kk])
                  sheet1.write(count, 1, "{}".format(houduan[k][kk]))
                  wb.save('111111test.xls')
                  cisu += 1
                elif kk == "jp":
                  jp.append(houduan[k][kk])  # 第二层的值
                  sheet1.write(count, 3, "{}".format(houduan[k][kk]))
                  count += 1
                  cisu += 1
            else:
                print("ddddddddddddddddddddddd")

wb.save("303后端.xlsx")
print(zh)
print(hk)
print(en)
print(jp)
