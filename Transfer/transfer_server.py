from Common.common_OpDB import  hh_DB

db = hh_DB('sxs_vault', '../config.ini')
#k=db.get_data("SELECT mobile FROM `vault_user_invest_trade_log` WHERE id = 72623")

def begin_tran(invest_id):
    sql_one="UPDATE vault_user_invest_trade_log SET  loan_time=date_sub(loan_time, interval 31 DAY) WHERE id=%s" % invest_id
    sql_two="UPDATE vault_user_repayment_log SET  date=date_sub(date, interval 35 DAY) WHERE invest_trade_log_id=%s LIMIT 1" %  invest_id
    db.get_data(sql_one)
    db.get_data(sql_two)


def end_tran(invest_id):
    sql_one="UPDATE vault_user_invest_trade_log SET  loan_time=date_add(loan_time, interval 31 DAY) WHERE id=%s" % invest_id
    sql_two="UPDATE vault_user_repayment_log SET  date=date_add(date, interval 35 DAY) WHERE invest_trade_log_id=%s LIMIT 1" %  invest_id
    db.get_data(sql_one)

def switch_tran(type,invest_id):
    if type =='begin':
        begin_tran(invest_id)
        return '搞定'
    else:
        end_tran(invest_id)
        return '搞定'
if __name__ =='__main__':
    end_tran(72623)
