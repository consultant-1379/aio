import numpy as np
kpi_constraints_dict = {"enb_init_gnb_mod_dur_wmean" : [0,np.inf],#?
"gnb_add_overall_duration_wmean": [0,np.inf],#?
"gnb_change_dur_wmean": [0,np.inf],#?
"gnb_init_gnb_mod_dur_wmean" : [0,np.inf],#?
'update_pdp_success_wmean' : [0,1],
'delete_pdp_success_wmean' : [0,1],
'ims_dereg_succ_ratio_wmean' : [0,1],
'ims_srvcc_succ_ratio_wmean' : [0,1],
'ims_reg_succ_ratio_wmean' : [0,1],
'ims_sess_change_succ_ratio_wmean' : [0,1],
'ims_rereg_succ_ratio_wmean' : [0,1],
'ims_sess_setup_succ_ratio_wmean' : [0,1],
'gnb_add_overall_succ_ratio_wmean' : [0,1],
'csfb_call_succ_wmean' : [0,1],
'srvcc_succ_ratio_wmean' : [0,1],
'attach_wmean'  : [0,1],
'lte_attach_wmean' : [0,1],
'ims_srvcc_delay_wmean' : [0,np.inf],#?
'ims_sess_change_delay_wmean' : [0,np.inf],#?
'ims_reg_delay_wmean' : [0,np.inf],#?
'ims_dereg_delay_wmean' : [0,np.inf],#?
'ims_call_setup_delay_wmean' : [0,np.inf],#?
'ims_rereg_delay_wmean' : [0,np.inf],#?
'rtp_delay_ul_wmean' : [0,np.inf],#?
'rtp_delay_dl_wmean' : [0,np.inf],#?
'harq_loss_dl_wmean' : [0,1],
'harq_loss_ul_wmean' : [0,1],
'rlc_loss_dl_wmean' : [0,1],
'rlc_loss_ul_wmean' : [0,1],
'pkt_loss_net_ul_wmean' : [0,1],
'pkt_loss_term_dl_wmean' : [0,1],
'pkt_loss_term_ul_wmean' : [0,1],
'pkt_loss_net_dl_wmean' : [0,1],
'rtp_packet_loss_dl_wmean' : [0,1],
'rtp_packet_loss_ul_wmean' : [0,1],
'pdcp_loss_dl_wmean' : [0,1],
'pdcp_loss_ul_wmean' : [0,1],
'pdcp_tp_dl_wmean' : [0,np.inf],#?
'pdcp_tp_ul_wmean' : [0,np.inf],#?
'tcp_tp_dl_wmean' : [0,np.inf],#?
'tcp_tp_ul_wmean' : [0,np.inf],#?
'rtt_net_wmean' : [0,np.inf],#?
'rtt_term_wmean' : [0,np.inf],#?
'udp_tp_class_ul_wmean' : [0,np.inf],#?
'udp_tp_class_dl_wmean' : [0,np.inf],#?
'tcp_tp_class_dl_wmean' : [0,np.inf],#?
'tcp_tp_class_ul_wmean' : [0,np.inf],#?
'delete_session_response_time_wmean': [0,np.inf],#?
's1_ho_wmean' : [0,1],
'abnormal_lte_conn_rel_ratio_wmean' : [0,1],
'create_session_wmean' : [0,1],
's1_ho_exec_time_wmean' : [0,np.inf],#?
'x2_ho_wmean' : [0,1],
'x2_ho_exec_time_wmean' : [0,np.inf],#?
'detach_wmean' :  [0,1],
'ims_abnorm_sess_rel_ratio_wmean' : [0,1],
'bytes_dl_sum' : [1,np.inf],
'bytes_ul_sum' : [1,np.inf],
'rsrp_wmean': [-140, -43],
'rsrq_wmean': [-19.5, -2.5],
'serving_rsrp_wmean': [-140, -43],
'serving_rsrq_wmean': [-19.5, -2.5],
'x2_ho_attempts_wmean' : [1,np.inf],
's1_ho_attempts_wmean' : [1,np.inf],
'ims_call_setup_time_wmean' : [0,np.inf],#?
'rtp_mos_dl_wmean' : [1,5],
'rtp_mos_ul_wmean' : [1,5],
'rtp_jitter_dl_wmean' : [0,np.inf],#?
'rtp_jitter_ul_wmean' : [0,np.inf],#?
"enb_init_gnb_mod_dur_sum" :[0, np.inf],
"gnb_add_overall_duration_sum":[0, np.inf],
"gnb_change_dur_sum":[0, np.inf],
"gnb_init_gnb_mod_dur_sum" :[0, np.inf],
'update_pdp_success_sum' :[0, np.inf],
'delete_pdp_success_sum' :[0, np.inf],
'ims_dereg_succ_ratio_sum' :[0, np.inf],
'ims_srvcc_succ_ratio_sum' :[0, np.inf],
'ims_reg_succ_ratio_sum' :[0, np.inf],
'ims_sess_change_succ_ratio_sum' :[0, np.inf],
'ims_rereg_succ_ratio_sum' :[0, np.inf],
'ims_sess_setup_succ_ratio_sum' :[0, np.inf],
'gnb_add_overall_succ_ratio_sum' :[0, np.inf],
'csfb_call_succ_sum' :[0, np.inf],
'srvcc_succ_ratio_sum' :[0, np.inf],
'attach_sum'  :[0, np.inf],
'lte_attach_sum' :[0, np.inf],
'ims_srvcc_delay_sum' :[0, np.inf],
'ims_sess_change_delay_sum' :[0, np.inf],
'ims_reg_delay_sum' :[0, np.inf],
'ims_dereg_delay_sum' :[0, np.inf],
'ims_call_setup_delay_sum' :[0, np.inf],
'ims_rereg_delay_sum' :[0, np.inf],
'rtp_delay_ul_sum' :[0, np.inf],
'rtp_delay_dl_sum' :[0, np.inf],
'harq_loss_dl_sum' :[0, np.inf],
'harq_loss_ul_sum' :[0, np.inf],
'rlc_loss_dl_sum' :[0, np.inf],
'rlc_loss_ul_sum' :[0, np.inf],
'pkt_loss_net_ul_sum' :[0, np.inf],
'pkt_loss_term_dl_sum' :[0, np.inf],
'pkt_loss_term_ul_sum' :[0, np.inf],
'pkt_loss_net_dl_sum' :[0, np.inf],
'rtp_packet_loss_dl_sum' :[0, np.inf],
'rtp_packet_loss_ul_sum' :[0, np.inf],
'pdcp_loss_dl_sum' :[0, np.inf],
'pdcp_loss_ul_sum' :[0, np.inf],
'pdcp_tp_dl_sum' :[0, np.inf],
'pdcp_tp_ul_sum' :[0, np.inf],
'tcp_tp_dl_sum' :[0, np.inf],
'tcp_tp_ul_sum' :[0, np.inf],
'rtt_net_sum' :[0, np.inf],
'rtt_term_sum' :[0, np.inf],
'udp_tp_class_ul_sum' :[0, np.inf],
'udp_tp_class_dl_sum' :[0, np.inf],
'tcp_tp_class_dl_sum' :[0, np.inf],
'tcp_tp_class_ul_sum' :[0, np.inf],
'delete_session_response_time_sum':[0, np.inf],
's1_ho_sum' :[0, np.inf],
'abnormal_lte_conn_rel_ratio_sum' :[0, np.inf],
'create_session_sum' :[0, np.inf],
's1_ho_exec_time_sum' :[0, np.inf],
'x2_ho_sum' :[0, np.inf],
'x2_ho_exec_time_sum' :[0, np.inf],
'detach_sum' :[0, np.inf],
'ims_abnorm_sess_rel_ratio_sum' :[0, np.inf],
'bytes_dl_sum' :[0, np.inf],
'bytes_ul_sum' :[0, np.inf],
'rsrp_sum':[0, np.inf],
'rsrq_sum':[0, np.inf],
'serving_rsrp_sum':[0, np.inf],
'serving_rsrq_sum':[0, np.inf],
'x2_ho_attempts_sum' :[0, np.inf],
's1_ho_attempts_sum' :[0, np.inf],
'ims_call_setup_time_sum' :[0, np.inf],
'rtp_mos_dl_sum' :[0, np.inf],
'rtp_mos_ul_sum' :[0, np.inf],
'rtp_jitter_dl_sum' :[0, np.inf],
'rtp_jitter_ul_sum' :[0, np.inf],
'tcp_tp_ul_sum' :[0, np.inf],
"enb_init_gnb_mod_dur_sample" :[0, np.inf],
"gnb_add_overall_duration_sample":[0, np.inf],
"gnb_change_dur_sample":[0, np.inf],
"gnb_init_gnb_mod_dur_sample" :[0, np.inf],
'update_pdp_success_sample' :[0, np.inf],
'delete_pdp_success_sample' :[0, np.inf],
'ims_dereg_succ_ratio_sample' :[0, np.inf],
'ims_srvcc_succ_ratio_sample' :[0, np.inf],
'ims_reg_succ_ratio_sample' :[0, np.inf],
'ims_sess_change_succ_ratio_sample' :[0, np.inf],
'ims_rereg_succ_ratio_sample' :[0, np.inf],
'ims_sess_setup_succ_ratio_sample' :[0, np.inf],
'gnb_add_overall_succ_ratio_sample' :[0, np.inf],
'csfb_call_succ_sample' :[0, np.inf],
'srvcc_succ_ratio_sample' :[0, np.inf],
'attach_sample'  :[0, np.inf],
'lte_attach_sample' :[0, np.inf],
'ims_srvcc_delay_sample' :[0, np.inf],
'ims_sess_change_delay_sample' :[0, np.inf],
'ims_reg_delay_sample' :[0, np.inf],
'ims_dereg_delay_sample' :[0, np.inf],
'ims_call_setup_delay_sample' :[0, np.inf],
'ims_rereg_delay_sample' :[0, np.inf],
'rtp_delay_ul_sample' :[0, np.inf],
'rtp_delay_dl_sample' :[0, np.inf],
'harq_loss_dl_sample' :[0, np.inf],
'harq_loss_ul_sample' :[0, np.inf],
'rlc_loss_dl_sample' :[0, np.inf],
'rlc_loss_ul_sample' :[0, np.inf],
'pkt_loss_net_ul_sample' :[0, np.inf],
'pkt_loss_term_dl_sample' :[0, np.inf],
'pkt_loss_term_ul_sample' :[0, np.inf],
'pkt_loss_net_dl_sample' :[0, np.inf],
'rtp_packet_loss_dl_sample' :[0, np.inf],
'rtp_packet_loss_ul_sample' :[0, np.inf],
'pdcp_loss_dl_sample' :[0, np.inf],
'pdcp_loss_ul_sample' :[0, np.inf],
'pdcp_tp_dl_sample' :[0, np.inf],
'pdcp_tp_ul_sample' :[0, np.inf],
'tcp_tp_dl_sample' :[0, np.inf],
'tcp_tp_ul_sample' :[0, np.inf],
'rtt_net_sample' :[0, np.inf],
'rtt_term_sample' :[0, np.inf],
'udp_tp_class_ul_sample' :[0, np.inf],
'udp_tp_class_dl_sample' :[0, np.inf],
'tcp_tp_class_dl_sample' :[0, np.inf],
'tcp_tp_class_ul_sample' :[0, np.inf],
'delete_session_response_time_sample':[0, np.inf],
's1_ho_sample' :[0, np.inf],
'abnormal_lte_conn_rel_ratio_sample' :[0, np.inf],
'create_session_sample' :[0, np.inf],
's1_ho_exec_time_sample' :[0, np.inf],
'x2_ho_sample' :[0, np.inf],
'x2_ho_exec_time_sample' :[0, np.inf],
'detach_sample' :[0, np.inf],
'ims_abnorm_sess_rel_ratio_sample' :[0, np.inf],
'bytes_dl_sample' :[0, np.inf],
'bytes_ul_sample' :[0, np.inf],
'rsrp_sample':[0, np.inf],
'rsrq_sample':[0, np.inf],
'serving_rsrp_sample':[0, np.inf],
'serving_rsrq_sample':[0, np.inf],
'x2_ho_attempts_sample' :[0, np.inf],
's1_ho_attempts_sample' :[0, np.inf],
'ims_call_setup_time_sample' :[0, np.inf],
'rtp_mos_dl_sample' :[0, np.inf],
'rtp_mos_ul_sample' :[0, np.inf],
'rtp_jitter_dl_sample' :[0, np.inf],
'rtp_jitter_ul_sample' :[0, np.inf],
'tcp_tp_ul_sample' :[0, np.inf]
                       }