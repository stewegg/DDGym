import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='DanL-v2',
    entry_point='gym_DanL.envs:DanLEnv',
)
