def json_list(x,ans):   
    if type(x) is dict:
        for a in x:
            ans.append(a)
            json_list(x[a],ans)
    else:
        ans.append(x)
        
    return ans

def list_json(x, json):
    if len(json) > 0:
        tmp = dict()
        tmp[x[0]] = json 
        json = tmp
        if len(x) == 1:
            return json
        else:
            return list_json(x[1:],json)
            
    else:
        json = x[0]
        return list_json(x[1:],json)
#########################################
input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}

def reverse(input_value):
    j2l = json_list(input_value,[])
    output_value = list_json( j2l, {})
    print( output_value )
    return output_value

