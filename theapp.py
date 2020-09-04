from flask import Flask, jsonify, abort


app=Flask(__name__)

panels=[
        {'no':1,
        'MANufacturer':'Coenergy',
        'MOdel':'JM-030',
        'Power (Watts)':'30',
        'Voltage':'12',
        'length':'666',
        'width':'421',
        'efficiency 0-1':'0.107'
        },
        {'no':2,
        'MANufacturer':'Coenergy',
        'MOdel':'C125PI',
        'Power (Watts)':'125',
        'Voltage':'12',
        'length':'1499',
        'width':'662',
        'efficiency 0-1':'0.126'
        },
        {'no':3,
        'MANufacturer':'Coenergy',
        'MOdel':'C175M',
        'Power (Watts)':'175',
        'Voltage':'24',
        'length':'1575',
        'width':'826',
        'efficiency 0-1':'0.135'
        },
        {'no':4,
        'MANufacturer':'JA Solar',
        'MOdel':'JAM6 60-250',
        'Power (Watts)':'250',
        'Voltage':'24',
        'length':'1650',
        'width':'991',
        'efficiency 0-1':'0.153'
        }]




@app.route('/panel/<int:req_no>',methods=['GET'])
def value(req_no):
    panel=[panel for panel in panels if panel['no']==req_no]
    if len(panel)==0:
        abort(404)
    return jsonify({'Solar Panel':panel[0]})



if __name__=='__main__':
    app.run() 
