import os

if __name__ == '__main__':
    # cmd = 'python tools/train.py configs/rpc/cascade_rcnn_r50_fpn_3x_rpc_proto5_1.py'
    # os.system(cmd)
    # cmd = 'python tools/test.py configs/rpc/cascade_rcnn_r50_fpn_3x_rpc_proto5_1.py ' \
    #       'result/cascade_rcnn_r50_fpn_3x_rpc_proto5_1/latest.pth --out ' \
    #       'result/cascade_rcnn_r50_fpn_3x_rpc_proto5_1/result.pkl --eval bbox '
    # os.system(cmd)
    # cmd = 'python rpc_eval.py --root ./result/cascade_rcnn_r50_fpn_3x_rpc_proto5_1/ '  # --score_thr 0.7
    # os.system(cmd)
    # cmd = 'python tools/test.py configs/rpc/cascade_rcnn_r50_fpn_3x_rpc_proto5_1.py ' \
    #       'result/cascade_rcnn_r50_fpn_3x_rpc_proto5_1/latest.pth --out ' \
    #       'result/cascade_rcnn_r50_fpn_3x_rpc_proto5_1/result.pkl --eval bbox '
    # os.system(cmd)
    # cmd = 'python rpc_eval2.py --root ./result/cascade_rcnn_r50_fpn_3x_rpc_proto5_1/ --result_name result1 --score_filter True'
    # os.system(cmd)

    # cmd = 'python tools/train.py configs/rpc/faster_rcnn_r50_fpn_1x_rpc_protoS_ranking_mll_no_bg.py'
    # os.system(cmd)
    # cmd = 'python tools/test.py configs/rpc/faster_rcnn_r50_fpn_1x_rpc_protoS_ranking_mll_no_bg.py ' \
    #       'result/faster_rcnn_r50_fpn_1x_rpc_protoS_ranking_mll_no_bg/latest.pth --out ' \
    #       'result/faster_rcnn_r50_fpn_1x_rpc_protoS_ranking_mll_no_bg/result.pkl'
    # os.system(cmd)
    # cmd = 'python rpc_eval.py --root ./result/faster_rcnn_r50_fpn_1x_rpc_protoS_ranking_mll_no_bg/'
    # os.system(cmd)

    # cmd = 'python tools/train.py configs/rpc/faster_rcnn_r50_fpn_3x_rpc_protoS_ranking_mll_e8.py'
    # os.system(cmd)
    # cmd = 'python tools/test.py configs/rpc/faster_rcnn_r50_fpn_3x_rpc_protoS_ranking_mll_e8.py ' \
    #       'result/faster_rcnn_r50_fpn_3x_rpc_protoS_ranking_mll_e8/latest.pth --out ' \
    #       'result/faster_rcnn_r50_fpn_3x_rpc_protoS_ranking_mll_e8/result1.pkl'
    # os.system(cmd)
    cmd = 'python rpc_eval.py --root ./result/faster_rcnn_r50_fpn_3x_rpc_protoS_ranking_mll_e8/ --result_name result1'
    os.system(cmd)
    #
    # cmd = 'python tools/train.py configs/rpc/faster_rcnn_r50_fpn_3x_rpc_proto4.py'
    # os.system(cmd)
    # cmd = 'python tools/test.py configs/rpc/faster_rcnn_r50_fpn_3x_rpc_proto4.py ' \
    #       'result/faster_rcnn_r50_fpn_3x_rpc_proto4/latest.pth --out ' \
    #       'result/faster_rcnn_r50_fpn_3x_rpc_proto4/result.pkl --eval bbox '
    # os.system(cmd)
    # cmd = 'python rpc_eval.py --root ./result/faster_rcnn_r50_fpn_3x_rpc_proto4/'
    # os.system(cmd)

    # cmd = 'python tools/test.py configs/rpc/cascade_rcnn_r50_fpn_1x_rpc.py
    # result/cascade_rcnn_r50_fpn_1x_rpc/latest.pth ' \ '--show-dir result/cascade_rcnn_r50_fpn_1x_rpc/imgs
    # --show-score-thr 0' os.system(cmd) cmd = 'python tools/test.py
    # configs/rpc/faster_rcnn_r50_fpn_1x_rpc.py ' \ 'result/faster_rcnn_r50_fpn_mstrain_1x_rpc/latest.pth
    # --show-dir result/faster_rcnn_r50_fpn_mstrain_1x_rpc/imgs '\ '--show-score-thr 0' os.system(cmd)
